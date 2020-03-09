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
from gridManipulations import *
from ecoNameManipulations import *
# Support functions

def santaBarbaraReader():
    df = pd.read_csv(basePath+'sbPredatorPreyMatrix.csv') 
    correctColumns = df.iloc[[1]].values.tolist()[0]
    for k,item in enumerate(correctColumns):
        if type(item) is not str:
            correctColumns[k] = "Unnamed"+str(k)
    
    df.columns = correctColumns
    new_columns = df.columns.values
    new_columns[1] = 'Species'
    df.columns = new_columns

    df = df.drop(df.index[0:2])
    df = df.drop(df.columns[130:],axis=1)
    df = df.drop(df.columns[0],axis=1)
    
    df["Species"] = df["Species"].str.lower()
    df.columns = [x.lower() for x in df.columns]

    return crushMatrixToDict(df)

def processGovPlantInteractions():
    df = pd.read_csv(basePath+"plantInsects.csv")
    #df.columns.values.tolist()
    df = df[["Insect species", "Flower Species"]]

    dfPollinators = df["Insect species"]
    dfPlants = df["Flower Species"]

    pollinators = list(set(dfPollinators.values.tolist()))
    pollinators = list(map(lambda x: cleanEcologicalName(x),pollinators))

    plants = list(set(dfPlants.values.tolist()))
    plants = list(map(lambda x: cleanEcologicalName(x),plants))

    return crushCoupledListToDict(pollinators,plants)

def leatherBritain():
    df = pd.read_excel(basePath+'leatherBritain.xls',header=None)

    combinedToSingleNameRow = defineNewRowHeaders(df)[1:]
    combinedToSingleNameCol = defineNewColHeaders(df,0,1)[1:]
    df = df.drop(df.columns[0:2],axis=1)
    df = df.drop(df.index[0:3])

    combinedToSingleNameRow.insert(0,'species')

    df.columns = combinedToSingleNameRow
    df['species'] = combinedToSingleNameCol

    return crushNonReciprocatedAdjList(df, verify=True)

def leatherFinland():
    df = pd.read_excel(basePath+'leatherFinland.xls',header=None)

    combinedToSingleNameRow = defineNewRowHeaders(df)[1:]
    combinedToSingleNameCol = defineNewColHeaders(df,0,1)[1:]
    df = df.drop(df.columns[0:2],axis=1)
    df = df.drop(df.index[0:3])

    combinedToSingleNameRow.insert(0,'species')

    df.columns = combinedToSingleNameRow
    df['species'] = combinedToSingleNameCol

    return crushNonReciprocatedAdjList(df, verify=True)

def readGovPollinator():
    df = pd.read_csv(basePath+'plantPollinator.csv')
    dfPollinators = df['POLLINATOR_NAME']
    dfPlants = df['PLANT_NAME']

    pollinators = list(set(dfPollinators.values.tolist()))
    pollinators = list(map(lambda x: cleanEcologicalName(x),pollinators))

    plants = list(set(dfPlants.values.tolist()))
    plants = list(map(lambda x: cleanEcologicalName(x),plants))

    return crushCoupledListToDict(pollinators,plants)
    
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

    combinedToSingleNameRow = defineNewRowHeaders(df)
    combinedToSingleNameCol = defineNewColHeaders(df,2,3)

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

def defineNewRowHeaders(df):
    firstNameRow = df.iloc[0].values.tolist()
    secondNameRow = df.iloc[1].values.tolist()
    combinesToTuples = list(zip(firstNameRow,secondNameRow))
    combinesToTuples = list(filter(lambda x: (type(x[0]) is str) and (type(x[1]) is str), combinesToTuples ))
    combinesToTuples = list(map(lambda x: (x[0], '') if "--" in x[1] else x, combinesToTuples))
    combinedToSingleNameRow = list(map(lambda x: (x[0].lower()+" "+x[1].lower()).strip(), combinesToTuples))

    return combinedToSingleNameRow

def defineNewColHeaders(df,firstIndex,secondIndex):
    namedCols = list(zip(df.iloc[:,firstIndex].values.tolist(),df.iloc[:,secondIndex].values.tolist()))
    namedCols = namedCols[2:]
    namedCols = list(map(lambda x: (x[0],'') if type(x[1]) is not str else x, namedCols))
    combinedToSingleNameCol = list(map(lambda x: (x[0].lower()+" "+x[1].lower()).strip(), namedCols))

    return combinedToSingleNameCol