###ISSUES PRESENTLY

##SOME INTERACTIONS ARE BEING MISSED DUE TO INCONSISTENCIES
##MAKE SURE TO SEARCH OVER ALL VALUES, NOT JUST FIRST?
##OR ONLY COUNT FIRST INTERACTIONS?

import pandas as pd
from collections import defaultdict
from data import validatedEiggData, eiggRawData
import os 
import re
import time
import pickle
from io import StringIO
import requests
from trophicMechanisms import *

basePath = "./RelevantDatasets/"
crushedDatasets = "./crushedFoodWebDatasets/"

def retrieveCollatedFoodWeb():
    ##NZ SB_DATA + DRYAD DATA GIVE NO IMPROVEMENT!
    #dataSetFunctions = [readFreshwaterData(), read2018GlobalDatabaseData(), readSantaBarbaraMatrix(), readSorensenData(), readJanesData(), readNZData(), readDryadData(), readEcoWeb()]
    coreDataSets = [readFreshwaterData(), read2018GlobalDatabaseData(), readSorensenData(), readJanesData(), readEcoWeb()]
    return aggregateDataSets(coreDataSets)

def readFreshwaterData():
    name = "freshWater"
    indivFoodWeb = {}
    if os.path.isfile(crushedDatasets+name):
        with open(crushedDatasets+name, 'rb') as f:
            indivFoodWeb = pickle.load(f)
    else:
        indivFoodWeb = crushPredatorPreyAdjListToDict('consumer','resource',basePath+'freshwater.csv',verify=False)
        with open(crushedDatasets+name, 'wb') as f:
            pickle.dump(indivFoodWeb,f)
    
    return indivFoodWeb

def read2018GlobalDatabaseData():
    name = "2018Global"
    indivFoodWeb = {}
    if os.path.isfile(crushedDatasets+name):
        with open(crushedDatasets+name, 'rb') as f:
            indivFoodWeb = pickle.load(f)
    else:
        indivFoodWeb = crushPredatorPreyAdjListToDict('con.taxonomy', 'res.taxonomy', basePath+'2018GlobAL.csv',verify=False)
        with open(crushedDatasets+name, 'wb') as f:
            pickle.dump(indivFoodWeb,f)
    
    return indivFoodWeb

def readEcoWeb():
    name = "EcoWeb"
    indivFoodWeb = {}
    if os.path.isfile(crushedDatasets+name):
        with open(crushedDatasets+name, 'rb') as f:
            indivFoodWeb = pickle.load(f)
    else:
        indivFoodWeb = prnFileReader()
        with open(crushedDatasets+name, 'wb') as f:
            pickle.dump(indivFoodWeb,f)
    
    return indivFoodWeb

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

def readDryadData():
    filesToProcess = getDryadFoodWebFiles()
    aggregated = []
    total = 0
    for f in filesToProcess:
        try:
            df = pd.read_excel(basePath+'/dryad/'+f, header=None)
            new_header = df.iloc[0] #grab the first row for the header
            df = df[1:] #take the data less the header row
            new_header[0] = "Species"
            df.columns = new_header #set the header row as the df header
            
            newCols = list(map(lambda x: standardiseNames(x), list(df.columns)))
            df = df.drop(df.filter(regex="unnamed:"),axis=1)
            newCols = list(filter(lambda x: "unnamed:" not in x,newCols))
            df.columns = newCols
            inter = list(df['species'])
            for k,i in enumerate(newCols[1:]):
                if standardiseNames(inter[k]) == i:
                    df.ix[k, 'species'] = i
                else:
                    df.ix[k, 'species'] ="f2tva25lgxq"
            df = df[df.species != 'f2tva25lgxq']
            invalidFollowing = len(df) - len(newCols)
            if invalidFollowing > 0:
                df.drop(df.tail(invalidFollowing).index,inplace=True) # drop last n rows

            dict_ = crushMatrixToDict(df)
            aggregated.append(dict_)
        except Exception as e:
            total += 1
        break
    
    return aggregateDataSets(aggregated)

def readNZData():
    filesToProcess = getNewZealandFoodWebFiles()
    aggregated = []
    total = 0
    for f in filesToProcess:
        try:
            df = pd.read_excel(basePath+'/newZealandAllPredatorPrey/'+f, header=None)
            new_header = df.iloc[0] #grab the first row for the header
            df = df[1:] #take the data less the header row
            new_header[0] = "Species"
            df.columns = new_header #set the header row as the df header
            
            newCols = list(map(lambda x: standardiseNames(x), list(df.columns)))
            df = df.drop(df.filter(regex="unnamed:"),axis=1)
            newCols = list(filter(lambda x: "unnamed:" not in x,newCols))
            df.columns = newCols

            df['species'] = newCols[1:]
            dict_ = crushMatrixToDict(df)
            aggregated.append(dict_)
        except Exception as e:
            total += 1

    print("Inconsistent blocks: " + str(total))
    return aggregateDataSets(aggregated)

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
    name = "janeData"
    indivFoodWeb = {}
    if os.path.isfile(crushedDatasets+name):
        with open(crushedDatasets+name, 'rb') as f:
            indivFoodWeb = pickle.load(f)
    else:
        indivFoodWeb = processJaneData()
        with open(crushedDatasets+name, 'wb') as f:
            pickle.dump(indivFoodWeb,f)
    
    return indivFoodWeb

def aggregateDataSets(datasets):
    totalConsumableAnimalsByPredator = defaultdict(set)

    for crushedDataset in datasets:
        for predator in crushedDataset:
            addAllPreyToDictSet(totalConsumableAnimalsByPredator[predator],crushedDataset[predator])    

    return totalConsumableAnimalsByPredator

def addAllPreyToDictSet(mainDictionarySubset, listOfAdditions):
    for item in listOfAdditions:
        mainDictionarySubset.add(item)


if __name__ == "__main__":
    print(len(readJanesData()))