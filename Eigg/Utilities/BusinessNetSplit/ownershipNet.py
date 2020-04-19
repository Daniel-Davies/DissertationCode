# Define an ownable organisation if it has equity to manage

# Heritage trust => Yes- ownership for the whole island + maintenance
# Clean planet now => No- they are focussed on "Exchanging" info etc
# Eigg electric => Yes- own the generators and land for them
# Eigg trading => By definition (real estate firm), which owns the shop, post office etc etc http://isleofeigg.org/ieht/ (subsidiary of eritage trust)
# Eigg construction => By definition (real estate firm), repsonsible for housing maintenance http://isleofeigg.org/ieht/
# Private houses for tourists => Yes
# Earth eco centre => For our purposes, no; it falls under heritage centre guidance, so nobody holds equity in it, but we'll say it "exchanges" knowledge?
# Samdavore farm => We'll say yes, since they own the farm and cattle (now Sandamore partnership)
# Eigg shop => Eigg trading owns it, sue and jacky are employees
# Taxi service => Hard to call equity; he provides more a service to the island
# Owners of craftshop are Hilda and Camille only => https://companycheck.co.uk/company/SC188634/THE-ISLE-OF-EIGG-CRAFTSHOP-LIMITED/companies-house-data
# Hebnet cic => yes; manage broadband connections

import sys
sys.path.insert(0,'./..')
from anonymisationTools import *

def ownershipGraph():
    return accessAnonymisedDataDict('ownershipGraph')

def getPoliticalOrgs():
    return ["Heritage Trust", "Eigg Trading", "Eigg Construction", "Eigg Electric"]

def getTouristOrgs():
    # Assumption; cafe is not tourism driven since residents will also regularly use
    return ["Craigard Teas", "Eigg Yurts", "TIGH AN SITHEAN", "Tophouse", "A NEAD KNITWEAR", "Selkie Explorers", "Eigg Adventures", "Eigg Camping Pods", "Kildonnan House", "Sweeney's Bothy", "The Bothy Cuagach", "Eigg Huts", "Eigg Shed", "Sweeney's Bothy", "Eddie's Eigg Croft", "Eigg Huts", "Glebe Barn", "Equilibrium Eigg Massage Therapy", "Eigg Organics", "Lagerona"]


def politicalNetwork():
    relationships = {}
    politicalOrgSet = set(getPoliticalOrgs())

    allRelationships = ownershipGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])

        relationships[person] = list(entireSet.intersection(politicalOrgSet))
    
    return relationships

def privateNetwork():
    relationships = {}
    politicalOrgSet = set(getPoliticalOrgs())

    allRelationships = ownershipGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])

        relationships[person] = list(entireSet - politicalOrgSet)
    
    return relationships

def involvedInPolitics():
    relationships = {}
    net = politicalNetwork()
    for item in net:
        relationships[item] = 1 if len(net[item]) > 0 else 0
    
    return relationships

def tourismNet():
    relationships = {}
    tourismOrgSet = set(getTouristOrgs())

    allRelationships = ownershipGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])
        relationships[person] = list(entireSet.intersection(tourismOrgSet))

    political = politicalNetwork()

    for item in relationships:
        if len(political[item]) == 0:
            relationships[item] = []

    return relationships

def fullTourismNet():
    relationships = {}
    tourismOrgSet = set(getTouristOrgs())

    allRelationships = ownershipGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])
        relationships[person] = list(entireSet.intersection(tourismOrgSet))

    return relationships

def nonTourismNet():
    relationships = {}
    tourismOrgSet = set(getTouristOrgs())

    allRelationships = ownershipGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])
        relationships[person] = list(entireSet - tourismOrgSet)

    political = politicalNetwork()

    for item in relationships:
        if len(political[item]) == 0:
            relationships[item] = []

    return relationships

def fullNonTourismNet():
    relationships = {}
    tourismOrgSet = set(getTouristOrgs())

    allRelationships = ownershipGraph()

    for person in allRelationships:
        entireSet = set(allRelationships[person])
        relationships[person] = list(entireSet - tourismOrgSet)

    political = politicalNetwork()

    return relationships

def involvedInTourism():
    relationships = {}
    tourismOrgSet = set(getTouristOrgs())
    net = ownershipGraph()
    for item in net:
        entireSet = set(net[item])
        relationships[item] = 1 if len(list(entireSet.intersection(tourismOrgSet))) > 0 else 0
    
    return relationships