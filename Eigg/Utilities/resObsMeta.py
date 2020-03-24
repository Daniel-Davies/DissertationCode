from data import *
import networkx as nx
from utils import seperationInMetres, toUsableLatLon

def retrieveRecorders(df):
    return list(filter(lambda x: type(x) == str,list(df['Recorder'].unique())))

def retrieveRecorderLocations(df):
    recorders = getKnownPeople()
    locs = {}
    df['Recorder'] = df['Recorder'].str.lower()
    for recorder in recorders:
        entries = df[df['Recorder'] == recorder]
        locations = list(zip(entries['Latitude (WGS84)'], entries['Longitude (WGS84)'], entries["Scientific name"]))
        locs[recorder] = locations
    
    return locs

def getKnownPeople():
    observers = lowerSet(set(retrieveRecorders(validatedEiggData())))
    allPeopleOnEigg = lowerSet(set(uninferredNamesGraph().keys()))

    observationPeople = observers.intersection(allPeopleOnEigg)
    return observationPeople

def locationsPerPerson():
    residences = {}

    residences['mairi mckinnon'] = [('56.9018832,-6.1449375', "Maranatha (7 Cleadale)")] # https://sjsa.wordpress.com/tag/eigg/s
    residences['neil robertson'] = [('56.922044,-6.1446842', "Eigg Organics")]
    residences['kenneth kean'] = [('56.8778059,-6.1337137','Pier Cottage')] # https://beta.companieshouse.gov.uk/company/SC554221/officers, http://isleofeigg.org/accommodation/the-smiddy/
    residences['bob wallace'] = [('56.8804647,-6.1417635', "Earth Connections Eco Centre")] # PROBABLY NOT REAL ADDRESS => https://beta.companieshouse.gov.uk/officers/x-151T1pEie2etTsFQ-zjg9LejI/appointments
    residences['george carr'] = [('56.9131675,-6.1619473', "Laig Farm")]
    residences['john booth'] = [('56.878903, -6.146895', "Galmisdale House")] #https://beta.companieshouse.gov.uk/company/SC170339/officers => I presume it means Galmisdale House
    residences['alex boden'] = [('56.8849159,-6.1415287', "Sandavore Farm")]
    residences['eddie scott'] = [('56.9222615,-6.1420233', "Eddie's Eigg Croft")]
    residences['pascal carr'] = [('56.918268, -6.154348', "Shore Cottage")]
    residences['stuart millar'] = [('56.9269519,-6.1439637', "Howlin House")]
    residences['colin carr'] = [('56.8889489,-6.1250917', "Kildonnan house")] 

    return residences

def lowerSet(setOfStrings):
    mutable = list(setOfStrings)
    mutable = list(map(lambda x: x.lower(),mutable))
    return set(mutable)

def buildObsResMetaNetwork():
    # peopleNameLocTuple = getKnownPeopleLocations() => Util only
    
    locationSet = locationsPerPerson()
    observationsKeyedOnRecorder = retrieveRecorderLocations(validatedEiggData())
    print(observationsKeyedOnRecorder)

    G = nx.Graph()
    names = locationSet.keys()
    animalLabels = createMeaningfulLabels(names, observationsKeyedOnRecorder)

    for name in names:
        G.add_node(name)
    
    print("First " + str(len(names)) + " nodes are group 1")
    
    for speciesLabel in animalLabels:
        G.add_node(speciesLabel)
    
    for nameKey in observationsKeyedOnRecorder:
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

def convertTripleToLocationKeys(keyedObs):
    locationKey = {}
    for name in keyedObs.keys():
        for lat,ln,species in keyedObs[name]:
            locationKey[species] = (lat,ln)
    
    return locationKey


    # get observation nodes & cross check against listed people
    # get residential nodes per person
    # link the two as a bipartite network
def createMeaningfulLabels(nameList, keyedObs):
    labelList = []
    seen = set()
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
                        entries[k] = (entry[0],entry[1],newLabel)
                        break 
                    iterator += 1
        
    return labelList

if __name__=="__main__":
    G = buildObsResMetaNetwork()
    #print(G.edges())