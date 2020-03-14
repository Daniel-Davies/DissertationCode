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

def ownershipGraph():
    relationships = {}
    
    relationships["Damian Helliwell"] = ["Heritage Trust"]
    relationships["Margaret Fyffe"] = ["Heritage Trust", "Eigg Electric", "Eigg Trading", "Eigg Construction", "The Bothy Cuagach"]

    relationships["Norah Barnes"] = ["Heritage Trust"]
    relationships["Elizabeth Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Shed", "Sandavore Farm", "Eigg Trading"]
    relationships["Lucy Conway"] = ["Heritage Trust", "Sweeney's Bothy", "Eddie's Eigg Croft"] #accountant, wife to eddie
    relationships["Sarah Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Electric", "Sandavore Farm", "Kildonnan Bay Oysters"]
    relationships["Mark Alan Foxwell"] = ["Heritage Trust"]
    relationships["Jacqueline Kirk"] = ["Heritage Trust"]
    relationships["Ian Leaver"] = ["Heritage Trust"]
    relationships["Stuart McCarthy"] = ["Glebe Barn","Heritage Trust", "Laig Bay Brewing", "Eigg Construction"] #supplies restaurants with beer 
    relationships["Tasha McVarish"] = ["Heritage Trust", "Equilibrium Eigg Massage Therapy"]
    
    relationships["Sue Hollands"] = ["Eigg Organics", "Eigg Electric"]
    relationships["Neil Robertson"] = ["Eigg Organics"]
    
    relationships["Sue Kirk"] = ["Lagerona", "Eigg Construction"] #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = ["Lagerona", "Eigg Construction"] ##INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = []
    relationships["Libby Galli"] = []
    
    relationships["Eddie Scott"] = ["Sweeney's Bothy", "Eddie's Eigg Croft", "Eigg Electric"]
    
    relationships["Marie Carr"] = ["Kildonnan House"]
    relationships["Colin Carr"] = ["Kildonnan House", "Eigg Electric", "Eigg Construction"]
    relationships["Greg Carr"] = ["Kildonnan House", "Eigg Trading"]
    
    relationships["Alex Boden"] = ["Eigg Shed", "Sandavore Farm", "Eigg Huts", "Hebnet Cic"]
    
    relationships["Katrin Bach"] = ["Eiggy Bread"] #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = ["Glebe Barn", "Eigg Construction"]
    
    relationships["Simon Helliwell"] = ["Hebnet Cic"] #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = [] #daughter is now technically owner

    relationships["Louise Taylor"] = []
    relationships["Martin Merrick"] = []
    relationships["Kenneth Kean"] = []
    relationships["Amanda Moult"] = []
    relationships["Annabelle Scott-Moncrieff"] = []
    relationships["Laraine Wyn-Jones"] = ["Eigg Adventures", "Eigg Camping Pods", "Eigg Trading"]
    relationships["Owain Wyn-Jones"] = ["Eigg Adventures", "Eigg Camping Pods"]
    
    relationships["John Christopher Lynch"] = ["LOST MAPS RECORDS LTD"]
    relationships["John Christopher Clare"] = ["Eigg Electric"]
    relationships["John Booth"] = ["Eigg Electric", "Eigg Construction"]
    
    relationships["George Carr"] = ["Laig Farm"] ##SHEEP FARMING
    relationships["Saira Renny"] = ["Laig Farm"]
    
    relationships["Bob Wallace"] = []
    
    relationships["Stuart Millar"] = []
    
    relationships["Jenny Robertson"] = ["A NEAD KNITWEAR"]
    
    relationships["Donna McCulloch"] = [] #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = ["Selkie Explorers"]
    
    ##basket making
    relationships["Catherine Davies"] = []
    relationships["Pascal Carr"] = []
    
    relationships["Stuart Fergusson"] = ["Eigg Trading", "Galmisdale Cafe"]
    
    relationships["Peter Wade-Martins"] = ["Tophouse"]
    relationships["Susanna Wade-Martins"] = ["Tophouse"]
    
    relationships["Jacky"] = ["TIGH AN SITHEAN"]
    relationships["Mick"] = ["TIGH AN SITHEAN"]
    
    relationships["Mairi McKinnon"] = []
    relationships["Clare Miller"] = ["Eigg Yurts"]
    
    relationships["John"] = ["Craigard Teas"]
    relationships["Sheila"] = ["Craigard Teas"] #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = ["Eigg History"]
    relationships["Hilda Ibrahim"] = []
    
    relationships["Ian Alexander James Bolas"] = ["Hebnet Cic"]
    relationships["David Byres Newton"] = ["Hebnet Cic"]
    relationships["Marc Allan Smith"] = ["Hebnet Cic"]
    
    relationships["Jennifer Leiper"] = []
    relationships["Robert Wallace"] = []
    relationships["Rosemary Jane Acock"] = []
    
    return relationships

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