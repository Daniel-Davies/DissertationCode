from data import validatedEiggData
import requests
import pickle
from collections import Counter
import pandas as pd
import numpy as np

basedir = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/Utilities/"
islandDatasets = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/IslandDatasets/"


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

    return taxonomicIndexs

def getSpeciesTaxonomicCategorty(name,category):
    with open("taxonomicIndexEigg", "rb") as f:
        ctx = pickle.load(f)

    groups,values = ctx[name]
    groups = groups.lower().split("|") 
    # ['', 'superkingdom', 'kingdom', 'phylum', 'subphylum', '', '', '', '', '', '', '', '', '', '', '', 'order', 'family', 'subfamily', '', 'genus', 'species']
    values = values.lower().split("|")

    taxonomy = dict(zip(groups,values))

    if category in taxonomy:
        return taxonomy[category]

def mapToValid(rawName,verifiedSpeciesDict):
    if rawName in verifiedSpeciesDict:
        return verifiedSpeciesDict[rawName]
    
    return rawName

def fetchCustomDataWithTaxonomy():
    with open(basedir+"crushedFoodWebDatasets/EiggVerifiedSpeciesList", "rb") as f:
        verifiedSpecies = pickle.load(f)

    data = pd.read_csv(islandDatasets+"eigg.csv") 
    df = data[['Recorder','Latitude (WGS84)', 'Longitude (WGS84)', 'Start date year', 'End date year', 'Scientific name', 'Common name', 'Family', 'Kingdom', 'Phylum', 'Class', 'Order', 'Genus']]

    df = df.dropna(subset=['Latitude (WGS84)'])
    df = df.dropna(subset=['Longitude (WGS84)'])
    df["Latitude (WGS84)"] = df["Latitude (WGS84)"].astype(np.float32)
    df["Longitude (WGS84)"] = df["Longitude (WGS84)"].astype(np.float32)

    df["Scientific name"] = df["Scientific name"].str.lower()
    df["Scientific name"] = df["Scientific name"].map(lambda x: mapToValid(x,verifiedSpecies))
    
    df = df.dropna(subset=['Start date year'])
    df["Start date year"] = df["Start date year"].astype(np.int32)

    return df

def consensusSelector(df,selector):
    df = df.dropna(subset=[selector])
    counted = Counter(df[selector].values.tolist())
    ret = (sorted(counted.items(),key=lambda x: x[1]))
    if len(ret) == 0:
        return ""
    try:
        s = ret[::-1][0][0].lower()
        return s
    except:
        print(ret[::-1][0][0])
        return ""

def measureDiffBetweenSources(taxonomicLevel):
    with open("taxonomicIndexEigg", "rb") as f:
        ctx = pickle.load(f)

    df = fetchCustomDataWithTaxonomy()
    df.columns = df.columns.str.lower()

    missingFromAPI = 0
    mismatchedWithFile = 0
    missingFromFile = 0
    errorCount = 0
    missingFromBoth = 0

    failures = set()

    for key in ctx:
        try:
            groups,values = ctx[key]
            groups = groups.lower().split("|") 
            values = values.lower().split("|")

            taxonomy = dict(zip(groups,values))
            if taxonomicLevel not in taxonomy:
                #specific = df[df["scientific name"] == key]
                #fileDriven = consensusSelector(specific,taxonomicLevel)
                missingFromAPI += 1

                specific = df[df["scientific name"]==key]
                fileConsensus = consensusSelector(specific,taxonomicLevel)
                if fileConsensus == "":
                    missingFromBoth += 1
                    missingFromFile += 1

            else:
                specific = df[df["scientific name"]==key]
                fileConsensus = consensusSelector(specific,taxonomicLevel)

                if taxonomy[taxonomicLevel] != fileConsensus:
                    if fileConsensus == "":
                        missingFromFile += 1
                    else:
                        mismatchedWithFile += 1
                        print(taxonomy[taxonomicLevel] + " ---- " + fileConsensus)
                        failures.add((taxonomy[taxonomicLevel], fileConsensus))
                    #print(taxonomy[taxonomicLevel] + " ---- " + consensusSelector(specific,taxonomicLevel))
        except Exception as e:
            missingFromAPI += 1
            errorCount += 1
        

    print()
    print("Missing from API: "+ str(missingFromAPI))
    print("Missing from file: "+ str(missingFromFile))
    print("Mismatches: "+ str(mismatchedWithFile))
    print("Error count: " + str(errorCount))
    print("Missing from both: " + str(missingFromBoth))
    print("Fail Cases: " + str(len(failures)))

def enrichTaxonomicLevelData(taxonomicLevel):
    pass

if __name__=="__main__":
    measureDiffBetweenSources("genus")
###TAXONOMY

# Domain => Genetic material, ~ 3 classes
# Kingdom => Animals, Plants, Fungi..
# Phylum => Body plan based e.g. "has a spine"
# Class => Mammals, Aves[birds] etc
# Order => e.g. Carnivores
# Family => e.g. Felidae (=Big Cats)
# Genus => e.g. Puma
# Species => e.g. Felis Catus (Genus + specific id)