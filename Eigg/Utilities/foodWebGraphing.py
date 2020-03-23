from data import validatedEiggData
from trophics import retrieveCollatedFoodWeb
import networkx as nx 
import pickle
from copy import deepcopy

basePath = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/EcoWebs/"

def graphFoodWeb(dateRange=(1700,2020), includeIsolates=False,  predatorSelector=(None, None), constraint=(None,None)):
    dataFrom, dataTo = dateRange

    verifiedEiggData = validatedEiggData() 
    constrainedEiggData = verifiedEiggData[(verifiedEiggData['Start date year'] >= dataFrom) & \
                                           (verifiedEiggData['Start date year'] < dataTo)]

    foodWeb = retrieveCollatedFoodWeb()

    if constraint[0] is not None:
        constrainedEiggData = constrainByTaxonomy(constrainedEiggData,constraint)

    if predatorSelector[0] is not None:
        foodWeb = constrainByPredators(foodWeb,predatorSelector)
    
    allScientificNames = constrainedEiggData['Scientific name'].values.tolist()
    allCommonNames = constrainedEiggData['Common name'].values.tolist()

    commonNameLabelMapping = dict(zip(allScientificNames,allCommonNames))

    G, labels = createTrophicGraph(constrainedEiggData, foodWeb)

    labelMapping = {}
    for item in labels:
        if type(commonNameLabelMapping[item]) is not str:
            labelMapping[item] = item
        else:
            labelMapping[item] = commonNameLabelMapping[item]

    if not includeIsolates:
        remove = [node for node,degree in G.degree() if degree == 0]
        G.remove_nodes_from(remove)
    
    return G, labelMapping

def constrainByTaxonomy(df, constraint):

    with open(basePath+"taxonomicIndexEigg", "rb") as f:
        taxonomicTree = pickle.load(f)
    
    return df[df.apply(lambda x: speciesMatchesConstraint(x['Scientific name'], constraint, taxonomicTree), axis=1)]

def constrainByPredators(foodWeb, constraint):

    with open(basePath+"taxonomicIndexEigg", "rb") as f:
        taxonomicTree = pickle.load(f)
    
    currentPredators = foodWeb.keys()
    newWeb = deepcopy(foodWeb)

    for predator in currentPredators:
        if not speciesMatchesConstraint(predator,constraint,taxonomicTree):
            del newWeb[predator]
    
    return newWeb

def speciesMatchesConstraint(record,constraint,taxonomicTree):
    if record not in taxonomicTree:
        return False

    constraintClass, constraintValue = constraint

    constraintClass = constraintClass.lower()
    constraintValue = constraintValue.lower()

    taxonomy = taxonomicTree[record]
    groups,values = taxonomy

    if groups is None or values is None:
        return False 
    elif groups == '' or values == '':
        return False

    groups = groups.lower().split("|")
    values = values.lower().split("|")
    indexedTreeCheck = dict(zip(groups,values))

    return constraintClass in indexedTreeCheck and \
           indexedTreeCheck[constraintClass] == constraintValue

def createTrophicGraph(df,foodWeb):
    G = nx.Graph()

    allPossibleSpecies = list(set(df['Scientific name'].values.tolist()))
    
    for i in allPossibleSpecies: 
        G.add_node(i)

    addEdgesToGraph(G,allPossibleSpecies,foodWeb)
    
    return G, allPossibleSpecies

def addEdgesToGraph(G,species,foodWeb):
    for s1 in species:
        predatorFoodWeb = foodWeb[s1]
        for s2 in species:
            if s1 != s2 and s2 in predatorFoodWeb:
                G.add_edge(s1,s2)
                