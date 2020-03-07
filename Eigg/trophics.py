
import pandas as pd
from collections import defaultdict
from data import validatedEiggData, eiggRawData

basePath = "./RelevantDatasets/"

def retrieveCollatedFoodWeb():
    dataSetFunctions = [readFreshwaterData(), read2018GlobalDatabaseData(), readSantaBarbaraMatrix(), readSorensenData(), readJanesData()]
    return aggregateDataSets(dataSetFunctions)

def readFreshwaterData():
    return crushPredatorPreyAdjListToDict('consumer','resource',basePath+'freshwater.csv')

def read2018GlobalDatabaseData():
    return crushPredatorPreyAdjListToDict('con.taxonomy', 'res.taxonomy', basePath+'2018GlobAL.csv')

def readSantaBarbaraMatrix():
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

def readSorensenData(): #done manually since there were small number of entries
    data = {}

    #headers: sambucus nigra, 'crataegus monogyna', 'rubus fruticosus', 'lonicera periclymenum', NANANAN, NANANA, 'circaea lutetiana', NANANA, 'rosa spinosissima', 'hedera helix', NANANANA, NANANANA 
    data["turdus merula"] = ['sambucus nigra', 'crataegus monogyna', 'rubus fruticosus', 'rosa spinosissima', 'hedera helix']   #blackbird
    data['turdus pilaris'] = ['crataegus monogyna'] #fieldfare
    data['turdus iliacus'] = ['sambucus nigra', 'crataegus monogyna'] #Redwing
    data['turdus philomelos'] = ['sambucus nigra', 'crataegus monogyna', 'rubus fruticosus', 'hedera helix'] #song thrush
    data['cyanistes caeruleus'] = ['sambucus nigra', 'rubus fruticosus', 'lonicera periclymenum'] #blue tit
    data['parus major'] = ['sambucus nigra'] #great tit
    data['aegithalos caudatus'] = [] #long tail tit
    data['sylvia atricapilla'] = ['sambucus nigra', 'circaea lutetiana', 'hedera helix'] #blackcap
    data['erithacus rubecula'] = ['sambucus nigra', 'hedera helix'] #robin
    data['columba palumbus'] = ['sambucus nigra', 'crataegus monogyna'] #woodpigeon
    data['pyrrhula pyrrhula'] = ['sambucus nigra', 'crataegus monogyna', 'lonicera periclymenum', 'rosa spinosissima', 'hedera helix'] #bullfinch
    data['fringilla coelebs'] = ['sambucus nigra'] #chaffinch

    return data

def readJanesData():
    eiggData = validatedEiggData()
    speciesCommonNames = eiggData["Common name"]
    speciesScientific = eiggData["Scientific name"]
    speciesCommonNames = speciesCommonNames.str.lower()
    speciesScientific = speciesScientific.str.lower()

    values = dict(list(set(zip(speciesCommonNames,speciesScientific))))
    print(len(values))

    df = pd.read_csv(basePath+'janePollinators.csv')

    combinedToSingleNameRow = defineNewRowHeadersJaneData(df)
    combinedToSingleNameCol = defineNewColHeadersJaneData(df)

    combinedToSingleNameRow = list(map(lambda x: values[x] if x in values else '', combinedToSingleNameRow))
    combinedToSingleNameColVals = list(map(lambda x: values[x] if x in values else '', combinedToSingleNameCol))

    df = df.drop(df.columns[0:3],axis=1)
    df = df.drop(df.columns[26:],axis=1)
    df = df.drop(df.index[0:2])

    combinedToSingleNameRow.insert(0,'species')

    df.columns = combinedToSingleNameRow

    columnEntryDict = dict(zip(combinedToSingleNameCol,combinedToSingleNameColVals))

    df['species'] = combinedToSingleNameColVals
    df = df.drop([""],axis=1)

    df = df[df['species'] != '']

    return crushNonReciprocatedAdjList(df)


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

def crushNonReciprocatedAdjList(df):
    predatorPreyDict = defaultdict(list)

    predatorSpeciesList = df["species"].values.tolist()
    preySpeciesList = df.columns[1:].values.tolist()

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

def crushPredatorPreyAdjListToDict(predatorColId, preyColId, filename):
    data = pd.read_csv(filename,encoding = "ISO-8859-1") 
    df = data[[preyColId, predatorColId]]

    df = df.dropna(subset=[preyColId])
    df = df.dropna(subset=[predatorColId])

    pairedUp = zip(df[predatorColId].str.lower(),df[preyColId].str.lower())

    groupedByPredator = defaultdict(list)
    for predator, prey in pairedUp:
        groupedByPredator[predator].append(prey)
    
    return groupedByPredator

def aggregateDataSets(datasets):
    totalConsumableAnimalsByPredator = defaultdict(set)

    for crushedDataset in datasets:
        for predator in crushedDataset:
            addAllPreyToDictSet(totalConsumableAnimalsByPredator[predator],crushedDataset[predator])    

    return totalConsumableAnimalsByPredator

def addAllPreyToDictSet(mainDictionarySubset, listOfAdditions):
    for item in listOfAdditions:
        mainDictionarySubset.add(item)
