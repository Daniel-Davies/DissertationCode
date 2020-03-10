from data import validatedEiggData
import requests
import pickle

def findType(groups,values,granularity=None):
    if granularity is None:
        return [groups,values]

    consumableGroup = groups.lower().split("|")
    consumableValues = values.lower().split("|")
    
    accessable = dict(zip(consumableGroup,consumableValues))
    if granularity in accessable:
        return accessable[granularity]
    else:
        return [groups,values]
    
def getSpeciesType(name, granularity=None):
    callToValidateName = requests.get('http://resolver.globalnames.org/name_resolvers.json?names='+name)
    try:
        jsonRes = callToValidateName.json()['data'][0]["results"][0]
        groups,values = jsonRes["classification_path_ranks"], jsonRes["classification_path"]
        return findType(groups,values,granularity)
    except:
        return ['','']

def groupDataByType(species,granularity):
    types = list(map(lambda x: getSpeciesType(x, granularity), species))
    return dict(zip(species,types))

# politeness function- avoid hitting servers manually every time
def buildEiggTaxonomicIndex():
    taxonomicIndex = {}
    speciesScientificNames = validatedEiggData()
    animals = set(speciesScientificNames["Scientific name"].values.tolist())
    total = 0
    for s in animals:
        taxonomicIndex[s] = getSpeciesType(s)
        total += 1
        if total % 100 == 0:
            print("Step: " + str(total))
    
    with open("taxonomicIndexEigg", "wb") as f:
        pickle.dump(taxonomicIndex,f)

    with open("taxonomicIndexEigg", "rb") as f:
        print(len(pickle.load(f)))

    return taxonomicIndex

print(len(buildEiggTaxonomicIndex()))
