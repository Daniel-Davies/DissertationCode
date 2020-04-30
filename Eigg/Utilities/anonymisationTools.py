
from faker import Factory
from collections import defaultdict
import pickle
import CollectedData
import os
from pathlib import Path 

basedir = os.path.split(os.path.abspath(__file__))[0]+"/AnonymisedDatasets/"

###########################
# Create a simple mapping for in memory data struct
##########################

def anonymise(dataIn):
    if isinstance(dataIn,str):
        newName = anonymiseSingleName(dataIn)
        return newName, {newName: dataIn}
    elif isinstance(dataIn,list):
        translated = list(map(lambda x: anonymiseSingleName(x), dataIn))
        return translated, dict(zip(translated,dataIn))
    elif isinstance(dataIn,dict):
        return anonymiseDictStruct(dataIn)
    
def anonymiseDictStruct(dataIn):
    fakeNameGen  = Factory.create()
    fakeNames  = defaultdict(fakeNameGen.name)

    consumable = dataIn.items()
    remade = []

    for i1,i2 in consumable:
        newI1 = fakeNames[i1]
        newI2 = fakeNames[i2]

        remade.append((newI1,newI2))
    
    return dict(zip([x[0] for x in remade],[x[1] for x in remade])), dict(fakeNames)

def anonymiseSingleName(name):
    if not isinstance(name,str): return name, {name:name}
    fakeNameGen  = Factory.create()
    fakeNames  = defaultdict(fakeNameGen.name)
    newName = fakeNames[name]
    return newName

#################################
## Internal tools
#################################

def anonymiseSensitiveData():
    writeDataStoreDirectory(constructAnonymousNameMapping())

def dontAnonymiseData():
    writeDataStoreDirectory(unitMapping())

def writeDataStoreDirectory(inMemMapping):
    if not os.path.exists(basedir):
        os.mkdir(basedir)
     
    for name, val in CollectedData.__dict__.items(): # iterate through every module's attributes
        if callable(val):                      # check if callable (normally functions)
            writeAnonymisedDict(val(),basedir+name, inMemMapping)  
    
    print("Functions ready to use Anonymous Data!")

def fakeListOfNames(data):
    fakeNameGen  = Factory.create()
    fakeNames  = defaultdict(fakeNameGen.name)
    for name in data:
        newName = fakeNames[name]
    
    return dict(fakeNames)

def anonymiseDataDict(rawData, inMemNameMapping):
    anonNames = inMemNameMapping

    allNames = list(rawData.keys())
    for name in allNames:
        if name in anonNames:
            newName = anonNames[name]
        else:
            newName = name
        oldNameValues = rawData.pop(name)
        rawData[newName] = oldNameValues
    
    for anonName in rawData:
        dataByName = rawData[anonName]
        if isinstance(dataByName, str):
            dataByName = cleanSingleString(dataByName, inMemNameMapping)
        elif isinstance(dataByName, list):
            if len(dataByName) > 0 and isinstance(dataByName[0],str):
                dataByName = cleanListOfStrings(dataByName, inMemNameMapping)
        
        rawData[anonName] = dataByName
        
    return rawData

def cleanSingleString(name, inMemNameMapping):
    anonNames = inMemNameMapping

    if name in anonNames:
        return anonNames[name]
    
    return name

def cleanListOfStrings(listOfNames, inMemNameMapping):
    return list(map(lambda x: cleanSingleString(x,inMemNameMapping), listOfNames))

def constructAnonymousNameMapping():
    fakeNameGen  = Factory.create()
    fakeNames  = defaultdict(fakeNameGen.name)
    data = CollectedData.uninferredNamesGraphRaw()
    for name in data:
        newName = fakeNames[name]
    
    fakeNames = dict(fakeNames)

    print("Names on Eigg anonymised!")
    
    return fakeNames

def unitMapping():
    data = CollectedData.uninferredNamesGraphRaw()
    mappingDict = {}
    for name in data:
        mappingDict[name] = name
    
    return mappingDict

def writeAnonymisedDict(originalDataDict, filename, inMemNameMapping):
    anonDataDict = anonymiseDataDict(originalDataDict, inMemNameMapping)

    with open(filename, 'wb') as f:
        pickle.dump(anonDataDict,f)

def accessAnonymisedDataDict(filename):
    with open(basedir+filename,'rb') as f:
        anonDataDict = pickle.load(f)

    return anonDataDict
