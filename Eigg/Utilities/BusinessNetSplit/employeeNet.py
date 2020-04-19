
import sys
sys.path.insert(0,'./..')
from anonymisationTools import *

def employeeGraph():
    return accessAnonymisedDataDict('employeeGraph')

def getPublicServices():
    return ["Clean Planet Now", "Eigg Eco Centre", "Eigg Primary School", "Roadworks", "Refuse Collection", "Health & Home Care"]

def publicEmployeeNetwork():
    relationships = {}
    publicServices = set(getPublicServices())

    allRelationships = employeeGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])

        relationships[person] = list(entireSet.intersection(publicServices))
    
    return relationships

def privateEmployeeNetwork():
    relationships = {}
    publicServices = set(getPublicServices())

    allRelationships = employeeGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])

        relationships[person] = list(entireSet - publicServices)
    
    return relationships

def involvedInPublicServices():
    relationships = {}
    net = publicEmployeeNetwork()
    for item in net:
        relationships[item] = 1 if len(net[item]) > 0 else 0
    
    return relationships