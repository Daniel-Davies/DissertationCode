
import pandas as pd
from collections import defaultdict

basePath = "./RelevantDatasets/"

def retrieveCollatedFoodWeb():
    dataSetFunctions = [readFreshwaterData(), read2018GlobalDatabaseData()]
    return aggregateDataSets(dataSetFunctions)

def readFreshwaterData():
    return crushPredatorPreyDataToDict('consumer','resource',basePath+'freshwater.csv')

def read2018GlobalDatabaseData():
    return crushPredatorPreyDataToDict('con.taxonomy', 'res.taxonomy', basePath+'2018GlobAL.csv')

def crushPredatorPreyDataToDict(predatorColId, preyColId, filename):
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
