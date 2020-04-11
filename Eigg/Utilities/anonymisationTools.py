
from faker import Factory
from collections import defaultdict
import pickle

def allRecordedNames():
    return ['Damian Helliwell', 'Margaret Fyffe', 'Norah Barnes', 'Elizabeth Boden', 'Lucy Conway', 'Sarah Boden', 'Mark Alan Foxwell', 'Jacqueline Kirk', 'Ian Leaver', 'Stuart McCarthy', 'Tasha McVarish', 'Sue Hollands', 'Neil Robertson', 'Sue Kirk', 'Alisdair Kirk', 'Charlie Galli', 'Libby Galli', 'Eddie Scott', 'Marie Carr', 'Colin Carr', 'Greg Carr', 'Alex Boden', 'Katrin Bach', 'Tamsin McCarthy', 'Simon Helliwell', 'Karen Helliwell', 'Louise Taylor', 'Martin Merrick', 'Kenneth Kean', 'Amanda Moult', 'Annabelle Scott-Moncrieff', 'Laraine Wyn-Jones', 'Owain Wyn-Jones', 'John Christopher Lynch', 'John Christopher Clare', 'John Booth', 'George Carr', 'Saira Renny', 'Bob Wallace', 'Stuart Millar', 'Jenny Robertson', 'Donna McCulloch', 'Celia Bull', 'Catherine Davies', 'Pascal Carr', 'Stuart Fergusson', 'Peter Wade-Martins', 'Susanna Wade-Martins', 'Jacky', 'Mick', 'Mairi McKinnon', 'Clare Miller', 'John', 'Sheila', 'Camille Dressler', 'Hilda Ibrahim', 'Ian Alexander James Bolas', 'David Byres Newton', 'Marc Allan Smith', 'Jennifer Leiper', 'Robert Wallace', 'Rosemary Jane Acock']

def anonymiseDataDict(rawData):
    with open('anonymisedNameMappings','rb') as f:
        anonNames = pickle.load(f)

    allNames = list(rawData.keys())
    for name in allNames:
        newName = anonNames[name]
        oldNameValues = rawData.pop(name)
        rawData[newName] = oldNameValues
    
    for anonName in rawData:
        dataByName = rawData[anonName]
        if isinstance(dataByName, str):
            dataByName = cleanSingleString(dataByName)
        elif isinstance(dataByName, list):
            if len(dataByName) > 0 and isinstance(dataByName[0],str):
                dataByName = cleanListOfStrings(dataByName)
        
        rawData[anonName] = dataByName
        
    return rawData

def cleanSingleString(name):
    with open('anonymisedNameMappings','rb') as f:
        anonNames = pickle.load(f)
    
    if name in anonNames:
        return anonNames[name]
    
    return name

def cleanListOfStrings(listOfNames):
    return list(map(cleanSingleString, listOfNames))

def constructAnonymousNameMapping():
    fakeNameGen  = Factory.create()
    fakeNames  = defaultdict(fakeNameGen.name)
    data = allRecordedNames()
    for name in data:
        newName = fakeNames[name]
    
    fakeNames = dict(fakeNames)
    
    with open('anonymisedNameMappings','wb') as f:
        pickle.dump(fakeNames,f)
    
    print("Names on Eigg anonymised!")

    # with open('anonymisedNameMappings','rb') as f:
    #     new = pickle.load(f)
    
    # print(new)

if __name__=="__main__":
    pass
    