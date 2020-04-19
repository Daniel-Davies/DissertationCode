from data import validatedEiggData
from trophics import retrieveCollatedFoodWeb
import networkx as nx 
import pickle
from copy import deepcopy

basePath = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/EcoWebs/"

def graphFoodWeb(dateRange=(1700,2020), includeIsolates=False,  predatorSelectors=[(None, None)], constraints=[(None,None)], specificity=None, directed=False):
    dataFrom, dataTo = dateRange

    verifiedEiggData = validatedEiggData() 
    constrainedEiggData = verifiedEiggData[(verifiedEiggData['Start date year'] >= dataFrom) & \
                                           (verifiedEiggData['Start date year'] < dataTo)]

    foodWeb = retrieveCollatedFoodWeb()

    for constraint in constraints:
        if constraint[0] is not None:
            constrainedEiggData = constrainByTaxonomy(constrainedEiggData,constraint)

    for predatorSelector in predatorSelectors:
        if predatorSelector[0] is not None:
            foodWeb = constrainByPredators(foodWeb,predatorSelector)
    
    allScientificNames = constrainedEiggData['Scientific name'].values.tolist()
    allCommonNames = constrainedEiggData['Common name'].values.tolist()

    commonNameLabelMapping = dict(zip(allScientificNames,allCommonNames))

    G, labels = createTrophicGraph(constrainedEiggData, foodWeb, specificity, directed)

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

def createTrophicGraph(df,foodWeb, specificity, directed):
    G = nx.Graph()
    if directed:
        G = nx.DiGraph()

    allPossibleSpecies = list(set(df['Scientific name'].values.tolist()))
    
    for i in allPossibleSpecies: 
        G.add_node(i)

    if specificity is None:
        addEdgesToGraph(G, allPossibleSpecies, foodWeb)
    else:
        addEdgesToGraphAbstracted(G, allPossibleSpecies, foodWeb, specificity)
    
    return G, allPossibleSpecies

def addEdgesToGraph(G, species, foodWeb):
    for s1 in species:
        predatorFoodWeb = foodWeb[s1]
        for s2 in species:
            if s1 != s2 and s2 in predatorFoodWeb:
                G.add_edge(s1,s2)

def addEdgesToGraphAbstracted(G, species, foodWeb, specificity):
    specifics = {}
    for item in species:
        try:
            specifics[item] = getTaxonomyForAnimal(item)[specificity]
        except:
            specifics[item] = ""

    mapping = {}
    for item in species:
        mapping[item] = set(mapToSpecifics(list(foodWeb[item]),specificity)) - set([""])
    
    for s1 in species:
        predatorFoodWebSpecified = mapping[s1]
        for s2 in species:
            if s1 != s2:
                val = specifics[s2]
                if val in predatorFoodWebSpecified:
                    G.add_edge(s1,s2)


def mapToSpecifics(species, specificity):
    with open(basePath+"taxonomicIndexEigg", "rb") as f:
        taxonomicTree = pickle.load(f)

    res = []
    for item in species:
        if item in taxonomicTree:
            taxonomy = taxonomicTree[item]
            groups,values = taxonomy

            groups = groups.lower().split("|")
            values = values.lower().split("|")
            indexedTreeCheck = dict(zip(groups,values))
            try:
                val = indexedTreeCheck[specificity]
                res.append(val)
            except:
                res.append("")
        else:
            res.append("")
    
    return res
                
def getTaxonomyForAnimal(species):
    with open(basePath+"taxonomicIndexEigg", "rb") as f:
        taxonomicTree = pickle.load(f)
    
    taxonomy = taxonomicTree[species]
    groups,values = taxonomy

    groups = groups.lower().split("|")
    values = values.lower().split("|")
    indexedTreeCheck = dict(zip(groups,values))

    return indexedTreeCheck
