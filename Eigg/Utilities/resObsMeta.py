from data import *
import networkx as nx
from utils import seperationInMetres, toUsableLatLon
from anonymisationTools import *

def buildObsResMetaNetwork():
    observationsKeyedOnRecorder = getIntersectionBetweenNBNAndNames()
    locationSet = locationsPerPerson()
    G = nx.Graph()
    names = locationSet.keys()
    animalLabels = createMeaningfulLabels(observationsKeyedOnRecorder)

    for name in names:
        G.add_node(name)
    
    print("First " + str(len(names)) + " nodes are group 1")
    
    for speciesLabel in animalLabels:
        G.add_node(speciesLabel)
        
    for nameKey in observationsKeyedOnRecorder:
        if nameKey not in names: continue # I don't have the addresses for some of the people in the observation set. skip these.
        entries = observationsKeyedOnRecorder[nameKey]
        for locationTuple in entries:
            G.add_edge(nameKey, locationTuple[2])
    
    locationTuplePerSpecies = convertTripleToLocationKeys(observationsKeyedOnRecorder)
    M = np.zeros((len(names),len(animalLabels)))

    for kName,name in enumerate(names):
        for kSpec, spec in enumerate(animalLabels):
            loc1 = toUsableLatLon(locationSet[name][0][0])
            loc2 = locationTuplePerSpecies[spec]
            M[kName,kSpec] = seperationInMetres(loc1,loc2)

    return G, M

def getIntersectionBetweenNBNAndNames():
    df = validatedEiggData() 
    df['Recorder'] = df['Recorder'].str.lower()
    observers = df.dropna(subset=['Recorder'])
    observers = observers["Recorder"]
    observers = list(observers)
    observers = set(list(map(lambda x: x.lower(), observers)))
    
    people = inferredNamesGraph()
    people = people.keys()
    people = set(list(map(lambda x: x.lower(), people))) - set(['john'])

    matching = []
    for p in people:
        for o in observers:
            if p in o:
                matching.append((p,o))
    
    locsIncluded = dict()
    uniqueNames = list(map(lambda x: x[0], matching))
    for u in uniqueNames:
        locsIncluded[u] = []
    
    for personOfInterest, actualEntry in matching:
        entries = df[df['Recorder'] == actualEntry]
        locations = list(zip(entries['Latitude (WGS84)'], entries['Longitude (WGS84)'], entries["Scientific name"]))
        locsIncluded[personOfInterest] += locations

    return locsIncluded

def getKnownPeople():
    observers = lowerSet(set(retrieveRecorders(validatedEiggData())))
    allPeopleOnEigg = lowerSet(set(uninferredNamesGraph().keys()))

    observationPeople = observers.intersection(allPeopleOnEigg) ##########
    return observationPeople

def locationsPerPerson():
    return accessAnonymisedDataDict('locationsPerPerson')

def lowerSet(setOfStrings):
    mutable = list(setOfStrings)
    mutable = list(map(lambda x: x.lower(),mutable))
    return set(mutable)

def convertTripleToLocationKeys(keyedObs):
    locationKey = {}
    for name in keyedObs.keys():
        for lat,ln,species in keyedObs[name]:
            locationKey[species] = (lat,ln)
    
    return locationKey

    # get observation nodes & cross check against listed people
    # get residential nodes per person
    # link the two as a bipartite network
def createMeaningfulLabels(keyedObs):
    labelList = []
    seen = set()
    nameList = keyedObs.keys()
    for name in nameList:
        entries = keyedObs[name]
        for k,entry in enumerate(entries):
            specificSpecies = entry[2]
            if specificSpecies not in seen:
                seen.add(specificSpecies)
                labelList.append(specificSpecies)
            else:
                iterator = 1
                while True:
                    newLabel = specificSpecies + " " + str(iterator)
                    if newLabel not in seen:
                        seen.add(newLabel)
                        labelList.append(newLabel)
                        keyedObs[name][k] = (entry[0],entry[1],newLabel)
                        break 
                    iterator += 1
        
    return labelList

if __name__=="__main__":
    G, M = buildObsResMetaNetwork()
    #print(G.edges())