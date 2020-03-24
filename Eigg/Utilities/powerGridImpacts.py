from data import validatedEiggData
from collections import defaultdict, Counter
from foodWebGraphing import constrainByTaxonomy

lowerYearBound = 1998
conversionYear = 2007

def getDataSamplesPerClass():
    beforeGrid = preGridData()
    afterGrid = postGridData()

    # print(len(beforeGrid), len(afterGrid)) => 12891 13864, so roughly equivalent

    familiesOfInterest = getFamiliesLikelyAffectedByGrid()
    animalsOfInterest = convertFamilyListToSpecies(familiesOfInterest)

    animalStatistics = measureEachAnimalNumbersByYear(animalsOfInterest)

    print("<>")

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

if __name__=="__main__":
    getDataSamplesPerClass()
