###ISSUES PRESENTLY

##SOME INTERACTIONS ARE BEING MISSED DUE TO INCONSISTENCIES
##MAKE SURE TO SEARCH OVER ALL VALUES, NOT JUST FIRST?
##OR ONLY COUNT FIRST INTERACTIONS?

import pandas as pd
from collections import defaultdict,Counter
from data import validatedEiggData, eiggRawData
import os 
import re
import time
import pickle
from io import StringIO
import requests
from trophicMechanisms import *

measured = []
basePath = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/Utilities/RelevantDatasets/production/"
crushedDatasets = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/Utilities/crushedFoodWebDatasets/"

def retrieveCollatedFoodWeb():
    #dataSetFunctions = [readFreshwaterData(), read2018GlobalDatabaseData(), readSantaBarbaraMatrix(), readSorensenData(), readJanesData(), readNZData(), readDryadData(), readEcoWeb()]
    coreDataSets = [readMangalDataset(), readCanberraWeb(), readFreshwaterData(), read2018GlobalDatabaseData(), readSorensenData(), readJanesData(), readEcoWeb(), readLeatherBritain(), readLeatherFinland(), readPlantPollinatorsUK(), govPlantInteractions()]
    # pickle.dump(aggregateDateSets(coreDataSets), open("aggregatedTrophics","wb"))
    return aggregateDataSets(coreDataSets)
    # return aggregateDataSetsAndMeasureReplicated(coreDataSets)

def invokeFunctionWithParameters(f,params):
    return f(*params)

def readCachedIndividualFoodwebs(name,f,params):
    indivFoodWeb = {}
    if os.path.isfile(crushedDatasets+name):
        with open(crushedDatasets+name, 'rb') as f:
            indivFoodWeb = pickle.load(f)
    else:
        indivFoodWeb = invokeFunctionWithParameters(f,params)
        with open(crushedDatasets+name, 'wb') as f:
            pickle.dump(indivFoodWeb,f)
    
    return indivFoodWeb

def readMangalDataset():
    return readCachedIndividualFoodwebs("mangalGlobal", mangalDatasetAPIInterface, [])

def readCanberraWeb():
    return readCachedIndividualFoodwebs("canberraWeb", canberraWebDataset,[])

def readLeatherBritain():
    return readCachedIndividualFoodwebs("leatherBritain",leatherBritain,[])

def readLeatherFinland():
    return readCachedIndividualFoodwebs("leatherFinland",leatherFinland,[])
    
def readFreshwaterData():
    return readCachedIndividualFoodwebs("freshWater",crushPredatorPreyAdjListToDict,['consumer','resource',basePath+'freshwater.csv',False])

def plantPollinatorGovDataset():
    return readCachedIndividualFoodwebs("govPlantPollinators", readGovPollinator, [])

def read2018GlobalDatabaseData():
    return readCachedIndividualFoodwebs("2018Global", crushPredatorPreyAdjListToDict, ['con.taxonomy', 'res.taxonomy', basePath+'2018GlobAL.csv',False])

def readEcoWeb():
    return readCachedIndividualFoodwebs("EcoWeb",prnFileReader,[])

def readPlantPollinatorsUK():
    return readCachedIndividualFoodwebs("plantPollinatorsGov", readGovPollinator, [])

def readSantaBarbaraMatrix():
    return readCachedIndividualFoodwebs("santaBarbara", santaBarbaraReader, [])

def readJanesData():
    return readCachedIndividualFoodwebs("janeData", processJaneData,[])

def govPlantInteractions():
    return readCachedIndividualFoodwebs("govPlantsInsects", processGovPlantInteractions,[])

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

def aggregateDataSetsAndMeasureReplicated(datasets):
    totalConsumableAnimalsByPredator = defaultdict(set)

    for crushedDataset in datasets:
        for predator in crushedDataset:
            addAllPreyToDictSetMeasured(predator,totalConsumableAnimalsByPredator[predator],crushedDataset[predator])    

    return totalConsumableAnimalsByPredator

def addAllPreyToDictSetMeasured(predator,mainDictionarySubset, listOfAdditions):
    global measured 
    for item in listOfAdditions:
        measured.append((predator,item))
        mainDictionarySubset.add(item)

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
    retrieveCollatedFoodWeb()

    #### COUNT THE NUMBER OF ONE TIME MEASURED INTERACTIONS
    ######################
    # print(len(list(filter(lambda x: x[1] < 3,Counter(measured).items()))))
    ############################
