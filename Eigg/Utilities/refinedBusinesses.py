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

def coOwnerNetworkRaw():
    relationships = {}
    
    relationships["Damian Helliwell"] = ["Heritage Trust"]
    relationships["Margaret Fyffe"] = ["Clean Planet Now", "Heritage Trust", "Eigg Electric", "Eigg Trading", "Eigg Construction", "The Bothy Cuagach"]
    relationships["Norah Barnes"] = ["Clean Planet Now", "Heritage Trust", "Eigg Eco Centre"]
    relationships["Elizabeth Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Shed", "Sandavore Farm", "Eigg Trading"]
    relationships["Lucy Conway"] = ["Heritage Trust", "Sweeney's Bothy", "Eddie's Eigg Croft"] #accountant, wife to eddie
    relationships["Sarah Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Electric", "Sandavore Farm", "Kildonnan Bay Oysters"]
    relationships["Mark Alan Foxwell"] = ["Heritage Trust"]
    relationships["Jacqueline Kirk"] = ["Heritage Trust"] #Sue is the owner of the shop => https://vimeo.com/81932195
    relationships["Ian Leaver"] = ["Heritage Trust"]
    relationships["Stuart McCarthy"] = ["Glebe Barn","Heritage Trust", "Laig Bay Brewing", "Eigg Construction"] #supplies restaurants with beer 
    relationships["Tasha McVarish"] = ["Heritage Trust", "Equilibrium Eigg Massage Therapy"]
    
    relationships["Sue Hollands"] = ["Eigg Organics", "Eigg Electric"]
    relationships["Neil Robertson"] = ["Eigg Organics"]
    
    relationships["Sue Kirk"] = ["Lagerona", "Eigg Construction"] #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = ["Lagerona", "Eigg Construction"] ##INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = ["Taxi Service"]
    relationships["Libby Galli"] = []
    
    relationships["Eddie Scott"] = ["Sweeney's Bothy", "Eddie's Eigg Croft", "Eigg Electric"]
    
    relationships["Marie Carr"] = ["Kildonnan House"]
    relationships["Colin Carr"] = ["Kildonnan House", "Eigg Electric", "Eigg Construction"]
    relationships["Greg Carr"] = ["Kildonnan House", "Eigg Trading"]
    
    relationships["Alex Boden"] = ["Eigg Shed", "Sandavore Farm", "Eigg Huts", "Hebnet Cic"]
    
    relationships["Katrin Bach"] = ["Eiggy Bread"] #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = ["Glebe Barn", "Eigg Construction"]
    
    relationships["Simon Helliwell"] = ["Glebe Barn", "Hebnet Cic"] #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = ["Glebe Barn"] #daughter is now technically owner

    relationships["Louise Taylor"] = []
    relationships["Martin Merrick"] = []
    relationships["Kenneth Kean"] = []
    relationships["Amanda Moult"] = []
    relationships["Annabelle Scott-Moncrieff"] = []
    relationships["Laraine Wyn-Jones"] = ["Eigg Adventures", "Eigg Camping Pods", "Eigg Trading"]
    relationships["Owain Wyn-Jones"] = ["Eigg Adventures", "Eigg Camping Pods"]
    
    #SAME GUY?!?!?!?!!?!?!
    relationships["John Christopher Lynch"] = ["LOST MAPS RECORDS LTD"]
    relationships["John Christopher Clare"] = ["Eigg Electric"]
    relationships["John Booth"] = ["Eigg Electric", "Eigg Construction"]
    
    relationships["George Carr"] = ["Laig Farm"] ##SHEEP FARMING
    relationships["Saira Renny"] = ["Laig Farm"]
    
    relationships["Bob Wallace"] = ["Eigg Eco Centre"]
    
    relationships["Stuart Millar"] = ["Fishing Co"]
    
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
    
    relationships["Jennifer Leiper"] = ["Clean Planet Now"]
    relationships["Robert Wallace"] = ["Clean Planet Now"]
    relationships["Rosemary Jane Acock"] = ["Clean Planet Now"]
    
    return relationships

def coOwnerNetwork():
    rawData = coOwnerNetworkRaw()
    return anonymiseDataDict(rawData)

def salesTagsCoOwnersRaw():
    relationships = {}
    
    relationships["Damian Helliwell"] = 0
    relationships["Margaret Fyffe"] = 1
    relationships["Norah Barnes"] = 0
    relationships["Elizabeth Boden"] = 1
    relationships["Lucy Conway"] = 1
    relationships["Sarah Boden"] = 1
    relationships["Mark Alan Foxwell"] = 0
    relationships["Jacqueline Kirk"] = 0 #Sue is the owner of the shop => https://vimeo.com/81932195
    relationships["Ian Leaver"] = 0
    relationships["Stuart McCarthy"] = 1
    relationships["Tasha McVarish"] = 1
    
    relationships["Sue Hollands"] = 1
    relationships["Neil Robertson"] = 1
    
    relationships["Sue Kirk"] = 1 #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = 1  #INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = 1
    relationships["Libby Galli"] = 0
    
    relationships["Eddie Scott"] = 1
    
    relationships["Marie Carr"] = 1
    relationships["Colin Carr"] = 1
    relationships["Greg Carr"] = 1
    
    relationships["Alex Boden"] = 1
    
    relationships["Katrin Bach"] = 0 #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = 1
    
    relationships["Simon Helliwell"] = 1 #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = 1 #daughter is now technically owner

    relationships["Louise Taylor"] = 0
    relationships["Martin Merrick"] = 0
    relationships["Kenneth Kean"] = 0
    relationships["Amanda Moult"] = 0
    relationships["Annabelle Scott-Moncrieff"] = 0
    relationships["Laraine Wyn-Jones"] = 1
    relationships["Owain Wyn-Jones"] = 1
    
    #SAME GUY?!?!?!?!!?!?!
    relationships["John Christopher Lynch"] = 0
    relationships["John Christopher Clare"] = 0  
    relationships["John Booth"] = 0
    
    relationships["George Carr"] = 0 ##SHEEP FARMING
    relationships["Saira Renny"] =  0
    
    relationships["Bob Wallace"] = 0
    
    relationships["Stuart Millar"] = 0
    
    relationships["Jenny Robertson"] = 0
    
    relationships["Donna McCulloch"] = 0 #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = 1
    
    ##basket making
    relationships["Catherine Davies"] = 0
    relationships["Pascal Carr"] = 0
    
    relationships["Stuart Fergusson"] = 1
    
    relationships["Peter Wade-Martins"] = 1
    relationships["Susanna Wade-Martins"] = 1
    
    relationships["Jacky"] = 1
    relationships["Mick"] = 1
    
    relationships["Mairi McKinnon"] = 0
    relationships["Clare Miller"] = 1
    
    relationships["John"] = 1
    relationships["Sheila"] = 1 #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = 0
    relationships["Hilda Ibrahim"] = 0
    
    relationships["Ian Alexander James Bolas"] = 0
    relationships["David Byres Newton"] = 0
    relationships["Marc Allan Smith"] = 0
    
    relationships["Jennifer Leiper"] = 0
    relationships["Robert Wallace"] = 0
    relationships["Rosemary Jane Acock"] = 0
    
    return relationships

def salesTagsCoOwners():
    rawData = salesTagsCoOwnersRaw()
    return anonymiseDataDict(rawData)

def tourismTags():
    pass 

def locationTags():
    pass
