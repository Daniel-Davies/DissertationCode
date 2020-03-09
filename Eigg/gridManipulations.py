
from collections import defaultdict
import pandas as pd
from ecoNameManipulations import *

def crushCoupledListToDict(predators,prey):
    predatorPreyDict = defaultdict(list)
    combines = list(zip(predators,prey))

    for predator, prey in combines:
        predatorPreyDict[predator].append(prey)
    
    return predatorPreyDict


def crushNonReciprocatedAdjList(df, verify=False):
    predatorPreyDict = defaultdict(list)

    predatorSpeciesList = df["species"].values.tolist()
    preySpeciesList = df.columns[1:].values.tolist()

    predatorSpeciesList = list(map(lambda x: cleanSpeciesName(x,verify), predatorSpeciesList))
    preySpeciesList = list(map(lambda x: cleanSpeciesName(x,verify), preySpeciesList))

    df['species'] = predatorSpeciesList
    
    df.set_index('species', inplace=True)

    for k, name in enumerate(predatorSpeciesList):
        animalRow = df.loc[[name]]
        for k,v in enumerate(preySpeciesList):
            try:
                if float(animalRow[v].values.tolist()[0]) > 0:
                    predatorPreyDict[name].append(v)
            except:
                pass #drop the invalid (duplicated) entries
    
    return predatorPreyDict

def crushMatrixToDict(df):
    predatorPreyDict = defaultdict(list)

    speciesList = list(df["species"])

    df.set_index('species', inplace=True)

    for k, name in enumerate(speciesList):
        animalRow = df.loc[[name]]
        for k,v in enumerate(speciesList):
            try:
                if float(animalRow[v].values.tolist()[0]) > 0:
                    predatorPreyDict[name].append(v)
            except:
                pass #drop the invalid (duplicated) entries
    
    return predatorPreyDict

def crushPredatorPreyAdjListToDict(predatorColId, preyColId, filename, verify):
    data = pd.read_csv(filename,encoding = "ISO-8859-1") 
    df = data[[preyColId, predatorColId]]

    df = df.dropna(subset=[preyColId])
    df = df.dropna(subset=[predatorColId])

    predators = df[predatorColId].values.tolist()
    prey = df[preyColId].values.tolist()

    predators = list(map(lambda x: cleanSpeciesName(x,verify), predators))
    prey = list(map(lambda x: cleanSpeciesName(x,verify), prey))

    pairedUp = zip(predators,prey)

    groupedByPredator = defaultdict(list)
    for predator, prey in pairedUp:
        groupedByPredator[predator].append(prey)
    
    return groupedByPredator