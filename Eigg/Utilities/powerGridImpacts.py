from data import validatedEiggData
from collections import defaultdict, Counter
from foodWebGraphing import constrainByTaxonomy, graphFoodWeb,getTaxonomyForAnimal
import pandas as pd  
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd
import networkx as nx
from math import sin, cos, sqrt, atan2, radians
from utils import *
from data import *
from resObsMeta import *
import seaborn as sns

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
    data = data[data['Start date year'] > conversionYear+1] # it was finished in february so just assume start of 2008 start => https://www.taylorhopkinson.com/eigg-ten-years-energy-independence/
    return data

def preGridData():
    data = validatedEiggData()
    data = data[data['Start date year'] >= lowerYearBound]
    data = data[data['Start date year'] < conversionYear+1]
    return data

def getFamiliesLikelyAffectedByGrid():
    # DONT ADD TOO MUCH TO DILUTE RESULTS

    # solar => https://infrastructure.planninginspectorate.gov.uk/wp-content/ipc/uploads/projects/EN010085/EN010085-000610-Appendix%204%20-%20Potential%20Ecological%20Impacts%20of%20Ground-Mounted%20Solar%20Panels.pdf
    # solar => http://publications.naturalengland.org.uk/file/6000213410447360
    # solar => http://migratorysoaringbirds.undp.birdlife.org/sites/default/files/RSPB%20Solar%20panel%20briefing.pdf    

    # wind => https://www.rspb.org.uk/our-work/our-positions-and-casework/our-positions/climate-change/action-to-tackle-climate-change/uk-energy-policy/wind-farms/
    # wind => https://en.wikipedia.org/wiki/Environmental_impact_of_wind_power#Impact_on_wildlife (shows tiny impact- 0.03 birds/ turbine killed)
    # wind => again tiny impact evidence (55mil to cats vs 106,000 to turbines) https://www.bbc.co.uk/news/science-environment-48936941

    # hydro => http://isleofeigg.org/eigg-electric/ (its a small hydro plant)
    # hydro => https://www.renewableenergyhub.co.uk/main/hydroelectricity-information/environmental-impact-of-hydroelectricity/ (doesnt look like much impact)
    # hydro => https://www.bbc.com/future/article/20170329-the-extraordinary-electricity-of-the-scottish-island-of-eigg (run of water plant)
    # hydro => it's a weir (https://www.youtube.com/watch?v=l3n-6YHquno) aka low dam

    # hydro => So it's really freshwater fish 
    # hydro => Doesn't look like there is going to be any fish there; but let's try anyway
    # hydro => check here for some https://www.nature.scot/plants-animals-and-fungi/fish/freshwater-fish
    # hydro => trout, salmon, sparling, arctic charr, allis shad
    
    # ref1 => provides names of the birds at risk that we use below (converted to family)
    # [ref1,ref1,ref1, then x2 wildlochaber.com/the-small-isles/wildlife/isle-of-eigg, bat on eigg, eagle (ref1 wind)]

    df = pd.read_csv("C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/IslandDatasets/eigg.csv")
    df = df.dropna(subset=['Start date year'])
    df = df.dropna(subset=['Family'])

    df = df[df["Start date year"]==2008]
    # df = df[df["Start date year"]>1895]
    df = df[df["Dataset ID"]=="dr528"]
    only = set(df['Family'].values.tolist())
    # rec = list(map(lambda x: (x, len(df[df['Dataset ID']==x])),list(only)))
    # rec[0]

    extrasOfResearch = set(["anatidae", "hirundinidae", "accipitridae","muscicapidae", "scolopacidae", "vespertilionidae", "accipitridae", "salmonidae", "osmeridae", "clupeidae", "gasterosteidae"])

    return list(only.union(extrasOfResearch))

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
    forward = 2018

    differences = {}

    while back < forward:
        rawBack = aggregated[back]
        rawForward = aggregated[forward]

        differences[str(back)+"-"+str(forward)] = list(map(lambda x: abs(rawBack[x]-rawForward[x]),range(len(labels))))
        back += 1
        forward -= 1

        if back == 2008: back += 1
        if forward == 2008: forward -= 1


    return differences, labels

def splitBetweenMiddle(dataset):
    aggregated, labels = aggregatedDataByYear(dataset)

    group1Crushable = list(map(lambda x: aggregated[x],range(1998,2008)))
    group2Crushable = list(map(lambda x: aggregated[x],range(2009,2019)))

    grp1crushed = [sum(list(x)) for x in zip(*group1Crushable)]
    grp2crushed = [sum(list(x)) for x in zip(*group2Crushable)]

    return grp1crushed, grp2crushed, labels

def aggregatedDataByYear(dataset):
    aggregated = defaultdict(list)

    yearRange = list(range(1998,2019)) 
    yearRange.remove(2008)

    labels = dataset.keys()
    for animal in labels:
        animalRecords = dataset[animal]
        for year in yearRange:
            if year in animalRecords:
                aggregated[year].append(dataset[animal][year])
            else:
                aggregated[year].append(0)

    # plug in re-translation to family here
    
    return aggregated, list(labels)


# BOX PLOT ON THE pairedOffDifferencesByYear function
# coloured bar charts with the splitBetweenMiddle function

if __name__=="__main__":
    grp1, grp2, labels = splitBetweenMiddle(getInteractivityPerAnimal())
    df = pd.DataFrame(columns=['Species name', 'Species count for range', 'Before installation?'])
    for i in range(len(grp1)):
        df.loc[i] = [labels[i],grp1[i],"False"]

    for i in range(len(grp2)):
        df.loc[i+len(grp1)] = [labels[i],grp2[i],"True"]

    pylab.rcParams['figure.figsize'] = (60.0, 45.0)

    g = sns.barplot(x="Species name", y="Species count for range", hue="Before installation?", data=df)
    g.set_xticklabels(g.get_xticklabels(),rotation=90,fontsize=8)
    g.set_yticklabels(g.get_yticklabels(),rotation=0,fontsize=8)
    plt.show()