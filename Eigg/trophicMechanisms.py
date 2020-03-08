import pandas as pd
from collections import defaultdict
from data import validatedEiggData, eiggRawData
import os 
import re
import time
import pickle
from io import StringIO
import requests
from trophics import *

## Grid Manipulations

def crushNonReciprocatedAdjList(df, verify=False):
    predatorPreyDict = defaultdict(list)

    predatorSpeciesList = df["species"].values.tolist()
    preySpeciesList = df.columns[1:].values.tolist()

    predatorSpeciesList = list(map(lambda x: cleanSpeciesName(x,verify), predatorSpeciesList))
    preySpeciesList = list(map(lambda x: cleanSpeciesName(x,verify), preySpeciesList))
    
    df.set_index('species', inplace=True)

    for k, name in enumerate(predatorSpeciesList):
        animalRow = df.loc[[name]]
        for k,v in enumerate(preySpeciesList):
            try:
                if float(animalRow[v].values.tolist()[0]) > 0:
                    predatorPreyDict[name].append(v)
            except:
                pass #drop the invalid (duplicated) entries
    
    return predatorPreyDict

def crushMatrixToDict(df):
    predatorPreyDict = defaultdict(list)

    speciesList = list(df["species"])

    df.set_index('species', inplace=True)

    for k, name in enumerate(speciesList):
        animalRow = df.loc[[name]]
        for k,v in enumerate(speciesList):
            try:
                if float(animalRow[v].values.tolist()[0]) > 0:
                    predatorPreyDict[name].append(v)
            except:
                pass #drop the invalid (duplicated) entries
    
    return predatorPreyDict

def crushPredatorPreyAdjListToDict(predatorColId, preyColId, filename, verify):
    data = pd.read_csv(filename,encoding = "ISO-8859-1") 
    df = data[[preyColId, predatorColId]]

    df = df.dropna(subset=[preyColId])
    df = df.dropna(subset=[predatorColId])

    predators = df[predatorColId].values.tolist()
    prey = df[preyColId].values.tolist()

    predators = list(map(lambda x: cleanSpeciesName(x,verify), predators))
    prey = list(map(lambda x: cleanSpeciesName(x,verify), prey))

    pairedUp = zip(predators,prey)

    groupedByPredator = defaultdict(list)
    for predator, prey in pairedUp:
        groupedByPredator[predator].append(prey)
    
    return groupedByPredator

# Support functions

def standardiseNames(name):
    name = name.replace('"', '')
    name = name.replace("'",'')
    name = name.replace("?",'')
    name = name.split("/")
    name = name[0]
    name = re.sub(r'\([^)]*\)', '', name)
    name = name.strip()
    name = name.lower()
    return name

def cleanSpeciesName(name, verify=True):
    name = cleanEcologicalName(name)
    if verify:
        name = validateSingleName(name)
    return name

def cleanEcologicalName(name):
    name = re.sub(r'\{.*\}', '', name)
    name = re.sub(r'\(.*\)', '', name)
    name = name.split(" ")

    if "cf" in name:
        name.remove("cf")
    
    if "cf." in name:
        name.remove("cf.")

    if "sp." in name:
        name.remove("sp.")

    if "spp." in name:
        name.remove("spp.")
    
    if "sp" in name:
        name.remove("sp")

    if "spp" in name:
        name.remove("spp")
    
    if "agg" in name:
        name.remove("agg")
    
    if "agg." in name:
        name.remove("agg.")

    if "indet" in name:
        name.remove("indet")
    
    if "indet." in name:
        name.remove("indet.")

    name = name[:2]
    name = " ".join(name)

    name = name.split("/")
    name = name[0]

    name = name.replace('"', '')
    name = name.replace("'",'')
    name = name.replace("?",'')

    return name.strip().lower()

def validateSingleName(name,limit=100):
    callToValidateName = requests.get('http://resolver.globalnames.org/name_resolvers.json?names='+name)
    jsonRes = callToValidateName.json()['data'][0]
    try:
        if not jsonRes['is_known_name']:
            return jsonRes['results']['canonical_form']
        else:
            return " ".join(name.split(" ")[:limit])
    except:
        print("Error occured at "+str(name))
        return name

    
def prnFileReader():
    eiggRawData = validatedEiggData()
    scientificNames = eiggRawData["Scientific name"].str.lower()
    commonNames = eiggRawData["Common name"].str.lower()
    convertCommonNameToScientific = dict(zip(commonNames,scientificNames))
    aggregated = []
    filesToProcess = getECOPath()
    aggregated = []
    for f in filesToProcess:
        with open("./prnTest/"+f, 'rb') as file_:
            content = (file_.readlines())

        fileId = getFileID(content[0])
        content = content[1:]
        if content[-1].decode("utf-8") == "\x1a":
            content = content[:-1]
        content = list(map(lambda x: x.strip().decode("utf-8"),content))
        content = list(map(lambda x: " ".join(x.split(" ")[1:]), content))

        content = list(map(lambda x: cleanSpeciesName(x,verify=False),content))
        matrixCorresponding = None
        try:
            with open("./RelevantDatasets/ECOWeB1.1/ECOWeB1.1/DATFILES/COMMUNITY/WEB"+fileId+".DAT", 'rb') as matrix:
                matrixCorresponding = matrix.readlines()
        except Exception as e:
            continue

        matrixCorresponding = matrixCorresponding[:-1]
        matrixCorresponding = list(map(lambda x: x.decode("utf-8").strip().split(" "),matrixCorresponding))
        matrixCorresponding = [list(filter(lambda y: len(y)>0,x)) for x in matrixCorresponding]
        matrixCorresponding = [list(map(lambda y: int(y),x)) for x in matrixCorresponding]
        matrixCorresponding = list(filter(lambda x: len(x)>0, matrixCorresponding))

        colHeader = matrixCorresponding[0][1:]
        rowHeader = list(map(lambda x: x[0],matrixCorresponding[1:]))

        content = list(map(lambda x: convertCommonNameToScientific[x] if x in convertCommonNameToScientific else x,content))

        colHeader = list(map(lambda x: content[x-1],colHeader))
        rowHeader = list(map(lambda x: content[x-1],rowHeader))

        matrixCorresponding = matrixCorresponding[1:]

        data = pd.DataFrame(matrixCorresponding,columns=["species"]+colHeader)
        data['species'] = data['species'].apply(lambda x: content[int(x)-1])
        aggregated.append(crushMatrixToDict(data))
    
        
    return aggregateDataSets(aggregated)

def getFileID(fileId):
    return standardiseNames(fileId.decode("utf-8")).split(" ")[0]

def getECOPath():
    return os.listdir('C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/prnTest')  

def getDryadFoodWebFiles():
    return os.listdir('C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/RelevantDatasets/dryad')

def getNewZealandFoodWebFiles():
    return os.listdir('C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/RelevantDatasets/newZealandAllPredatorPrey')

def processJaneData():
    eiggData = validatedEiggData()
    speciesCommonNames = eiggData["Common name"]
    speciesScientific = eiggData["Scientific name"]
    speciesCommonNames = speciesCommonNames.str.lower()
    speciesScientific = speciesScientific.str.lower()

    values = dict(list(set(zip(speciesCommonNames,speciesScientific))))

    df = pd.read_csv(basePath+'janePollinators.csv')

    combinedToSingleNameRow = defineNewRowHeadersJaneData(df)
    combinedToSingleNameCol = defineNewColHeadersJaneData(df)

    combinedToSingleNameRow = list(map(lambda x: values[x] if x in values else '', combinedToSingleNameRow))
    combinedToSingleNameCol = list(map(lambda x: values[x] if x in values else '', combinedToSingleNameCol))

    df = dropUselessGridPieces(df)

    combinedToSingleNameRow.insert(0,'species')

    df.columns = combinedToSingleNameRow

    df['species'] = combinedToSingleNameCol
    df = df.drop([""],axis=1)

    df = df[df['species'] != '']

    return crushNonReciprocatedAdjList(df, verify=True)

def dropUselessGridPieces(df):
    df = df.drop(df.columns[0:3],axis=1)
    df = df.drop(df.columns[26:],axis=1)
    df = df.drop(df.index[0:2])

    return df

def defineNewRowHeadersJaneData(df):
    firstNameRow = df.iloc[0].values.tolist()
    secondNameRow = df.iloc[1].values.tolist()
    combinesToTuples = list(zip(firstNameRow,secondNameRow))
    combinesToTuples = list(filter(lambda x: (type(x[0]) is str) and (type(x[1]) is str), combinesToTuples ))
    combinesToTuples = list(map(lambda x: (x[0], '') if "--" in x[1] else x, combinesToTuples))
    combinedToSingleNameRow = list(map(lambda x: (x[0].lower()+" "+x[1].lower()).strip(), combinesToTuples))

    return combinedToSingleNameRow

def defineNewColHeadersJaneData(df):
    namedCols = list(zip(df.iloc[:,2].values.tolist(),df.iloc[:,3].values.tolist()))
    namedCols = namedCols[2:]
    namedCols = list(map(lambda x: (x[0],'') if type(x[1]) is not str else x, namedCols))
    combinedToSingleNameCol = list(map(lambda x: (x[0].lower()+" "+x[1].lower()).strip(), namedCols))

    return combinedToSingleNameCol