
from faker import Factory
from collections import defaultdict
import pickle
import sensitiveData

basedir = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/Utilities/AnonymisedDatasets/"


def anonymiseDataDict(rawData, inMemNameMapping):
    anonNames = inMemNameMapping

    allNames = list(rawData.keys())
    for name in allNames:
        newName = anonNames[name]
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
    data = sensitiveData.uninferredNamesGraphRaw()
    for name in data:
        newName = fakeNames[name]
    
    fakeNames = dict(fakeNames)

    print("Names on Eigg anonymised!")
    
    return fakeNames

    # with open('anonymisedNameMappings','rb') as f:
    #     new = pickle.load(f)
    
    # print(new)

def anonymiseSensitiveData():
    inMemNameMapping = constructAnonymousNameMapping() #needs the "sensitiveData" file or it won't build
     
    for name, val in sensitiveData.__dict__.items(): # iterate through every module's attributes
        if callable(val):                      # check if callable (normally functions)
            writeAnonymisedDict(val(),basedir+name, inMemNameMapping)  
    
    print("Functions ready to use Anonymous Data!")

def writeAnonymisedDict(originalDataDict, filename, inMemNameMapping):
    anonDataDict = anonymiseDataDict(originalDataDict, inMemNameMapping)

    with open(filename, 'wb') as f:
        pickle.dump(anonDataDict,f)

def accessAnonymisedDataDict(filename):
    with open(basedir+filename,'rb') as f:
        anonDataDict = pickle.load(f)

    return anonDataDict

if __name__=="__main__":
    anonymiseSensitiveData()
    