from data import validatedEiggData
from collections import defaultdict, Counter
from foodWebGraphing import constrainByTaxonomy, graphFoodWeb

lowerYearBound = 1998
conversionYear = 2007

def getInteractivityPerAnimal(granularity=1):
    familiesOfInterest = getFamiliesLikelyAffectedByGrid()
    animalsOfInterest = convertFamilyListToSpecies(familiesOfInterest)

    degreeByAnimalByYear = defaultdict(dict)

    for year in range(lowerYearBound, 2021, granularity):
        G,mapping = graphFoodWeb(dateRange=(year,year+granularity))
        degreeMap = dict(G.degree())
        for animal in animalsOfInterest:
            if animal in degreeMap:
                degreeByAnimalByYear[animal][year] = degreeMap[animal]
            else:
                degreeByAnimalByYear[animal][year] = 0
 
    return degreeByAnimalByYear

def getRawOccurencesPerAnimalByYear():
    # beforeGrid = preGridData()
    # afterGrid = postGridData()

    # print(len(beforeGrid), len(afterGrid)) => 12891 13864, so roughly equivalent

    familiesOfInterest = getFamiliesLikelyAffectedByGrid()
    animalsOfInterest = convertFamilyListToSpecies(familiesOfInterest)

    animalStatistics = measureEachAnimalNumbersByYear(animalsOfInterest)

    return animalStatistics

def postGridData():
    data = validatedEiggData()
    data = data[data['Start date year'] >= conversionYear+1] # it was finished in february so just assume start of 2008 start => https://www.taylorhopkinson.com/eigg-ten-years-energy-independence/
    return data

def preGridData():
    data = validatedEiggData()
    data = data[data['Start date year'] >= lowerYearBound]
    data = data[data['Start date year'] < conversionYear+1]
    return data

def getFamiliesLikelyAffectedByGrid():
    return ["delphinidae"]

def convertFamilyListToSpecies(familiesList):
    df = validatedEiggData()
    animalsList = []
    for family in familiesList:
        concrete = (list(set(constrainByTaxonomy(df, ("Family", family))['Scientific name'])))
        for c in concrete:
            animalsList.append(c)
    
    return animalsList

def measureEachAnimalNumbersByYear(animals):
    animalByYearSummary = {}

    data = validatedEiggData()

    for animal in animals:
        filteredByAnimal = data[data['Scientific name'] == animal]
        yearsOfOccurence = Counter(filteredByAnimal['Start date year'])
        animalByYearSummary[animal] = yearsOfOccurence

    return animalByYearSummary



############################## GRAPHING ############################

def pairedOffDifferencesByYear(dataset):
    aggregated, labels = aggregatedDataByYear(dataset)

    back = 1998
    forward = 2017

    differences = {}

    while back < forward:
        rawBack = aggregated[back]
        rawForward = aggregated[forward]

        differences[str(back)+"-"+str(forward)] = list(map(lambda x: abs(rawBack[x]-rawForward[x]),range(len(labels))))
        back += 1
        forward -= 1


    return differences, labels

def splitBetweenMiddle(dataset):
    aggregated, labels = aggregatedDataByYear(dataset)

    group1Crushable = list(map(lambda x: aggregated[x],range(1998,2008)))
    group2Crushable = list(map(lambda x: aggregated[x],range(2008,2018)))

    grp1crushed = [sum(list(x)) for x in zip(*group1Crushable)]
    grp2crushed = [sum(list(x)) for x in zip(*group2Crushable)]

    return grp1crushed, grp2crushed, labels

def aggregatedDataByYear(dataset):
    aggregated = defaultdict(list)

    yearRange = range(1998,2018)

    labels = dataset.keys()
    for animal in labels:
        animalRecords = dataset[animal]
        for year in yearRange:
            if year in animalRecords:
                aggregated[year].append(dataset[animal][year])
            else:
                aggregated[year].append(0)
    
    return aggregated, list(labels)


if __name__=="__main__":
    print(splitBetweenMiddle(getRawOccurencesPerAnimalByYear()))

    