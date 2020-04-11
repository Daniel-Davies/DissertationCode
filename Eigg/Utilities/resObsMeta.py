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
    residences = {}

    residences['Mairi McKinnon'] = [('56.9018832,-6.1449375', "Maranatha (7 Cleadale)")] # https://sjsa.wordpress.com/tag/eigg/s
    residences['Neil Robertson'] = [('56.922044,-6.1446842', "Eigg Organics")]
    residences['Kenneth Kean'] = [('56.8778059,-6.1337137','Pier Cottage')] # https://beta.companieshouse.gov.uk/company/SC554221/officers, http://isleofeigg.org/accommodation/the-smiddy/
    residences['Bob Wallace'] = [('56.8804647,-6.1417635', "Earth Connections Eco Centre")] # PROBABLY NOT REAL ADDRESS => https://beta.companieshouse.gov.uk/officers/x-151T1pEie2etTsFQ-zjg9LejI/appointments
    residences['George Carr'] = [('56.9131675,-6.1619473', "Laig Farm")]
    residences['John Booth'] = [('56.878903, -6.146895', "Galmisdale House")] #https://beta.companieshouse.gov.uk/company/SC170339/officers => I presume it means Galmisdale House
    residences['Alex Boden'] = [('56.8849159,-6.1415287', "Sandavore Farm")]
    residences['Eddie Scott'] = [('56.9222615,-6.1420233', "Eddie's Eigg Croft")]
    residences['Pascal Carr'] = [('56.918268, -6.154348', "Shore Cottage")]
    residences['stuart Millar'] = [('56.9269519,-6.1439637', "Howlin House")]
    residences['Colin Carr'] = [('56.8889489,-6.1250917', "Kildonnan house")]
    residences['Marie Carr'] = [('56.8889489,-6.1250917', "Kildonnan house")]
    residences['Simon Helliwell'] = [('56.8902145,-6.1343823', "Glebe Barn")] #ok technically they USED to live here, but thats fine since thats when a lot of observations will overlap anyway
    residences['Karen Helliwell'] = [('56.8902145,-6.1343823', "Glebe Barn")]
    residences['Katrin Bach'] = [('56.9113759,-6.1654777', "Laig")] # https://en-gb.facebook.com/EiggyBread/

    # residences['stuart fergusson'] #couldn't get address
    # residences['jenny robertson'] #couldn't get address

    return residences

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