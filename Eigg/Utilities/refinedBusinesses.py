from data import *
from anonymisationTools import *

def exchangeNetwork():
    #crafts and primary fr, sue kirk exchnage with kildonnan, breqing guy to lagerona and cafe, katrin back for glebe barn
    #employees defined as an exchange relationship, not ownership relationship [who owns show?]
    exchaneNet = {}
    ownershipNet = coOwnerNetwork()
    allRelationships = uninferredNamesGraph()

    assert(len(ownershipNet) == len(allRelationships))

    for person in allRelationships:
        entireSet = set(allRelationships[person])
        ownerSet = set(ownershipNet[person])

        exchaneNet[person] = list(entireSet - ownerSet)
    
    return exchaneNet

def getPoliticalOrgs():
    return ["Heritage Trust", "Eigg Trading", "Eigg Construction"]

def politicalNetwork():
    relationships = {}
    politicalOrgSet = set(getPoliticalOrgs())

    allRelationships = inferredNamesGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])

        relationships[person] = list(entireSet.intersection(politicalOrgSet))
    
    return relationships

def involvedInPolitics():
    relationships = {}
    politicalOrgs = getPoliticalOrgs()
    net = coOwnerNetwork()
    for item in net:
        relationships[item] = 1 if len(set(net[item]).intersection(politicalOrgs)) > 0 else 0
    
    return relationships

def coOwnerNetwork():
    return accessAnonymisedDataDict('coOwnerNetworkRaw')

def salesTagsCoOwners():
    return accessAnonymisedDataDict('salesTagsCoOwnersRaw')

def exportTags():
    return accessAnonymisedDataDict('exportTags')