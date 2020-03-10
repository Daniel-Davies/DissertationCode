from data import validatedEiggData
from trophics import retrieveCollatedFoodWeb
import networkx as nx 
import pickle
from copy import deepcopy

def graphFoodWeb(dateRange=(1700,2020), isolates=False,  predatorSelector=(None, None), constraint=(None,None)):
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

    G = createTrophicGraph()
    
    return []

def constrainByTaxonomy(df, constraint):

    with open("taxonomicIndexEigg", "rb") as f:
        taxonomicTree = pickle.load(f)
    
    return df[df.apply(lambda x: speciesMatchesConstraint(x['Scientific name'], constraint, taxonomicTree), axis=1)]

def constrainByPredators(foodWeb, constraint):

    with open("taxonomicIndexEigg", "rb") as f:
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
           indexedTreeCheck[constraintClass.lower()] == constraintValue.lower()

def createTrophicGraph():
    return nx.Graph()

print(graphFoodWeb())