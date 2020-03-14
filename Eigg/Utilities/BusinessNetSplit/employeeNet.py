
def employeeGraph():
    relationships = {}
    
    relationships["Damian Helliwell"] = ["Eigg Crafts"]
    relationships["Margaret Fyffe"] = ["Clean Planet Now"]
    relationships["Norah Barnes"] = ["Clean Planet Now",  "Eigg Eco Centre"]
    relationships["Elizabeth Boden"] = ["Eigg Primary School"]
    relationships["Lucy Conway"] = [ "Lagerona", "Eigg Primary School"] #accountant, wife to eddie
    relationships["Sarah Boden"] = []
    relationships["Mark Alan Foxwell"] = []
    relationships["Jacqueline Kirk"] = ["Eigg Shop"]
    relationships["Ian Leaver"] = []
    relationships["Stuart McCarthy"] = [] #supplies restaurants with beer 
    relationships["Tasha McVarish"] = [ "Eigg Primary School"]   
    relationships["Sue Hollands"] = []
    relationships["Neil Robertson"] = ["Roadworks"]
    
    relationships["Sue Kirk"] = ["Eigg Shop"] #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = [] ##INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = ["Taxi Service"]
    relationships["Libby Galli"] = ["Eigg Crafts"]
    
    relationships["Eddie Scott"] = []
    
    relationships["Marie Carr"] = []
    relationships["Colin Carr"] = []
    relationships["Greg Carr"] = []
    
    relationships["Alex Boden"] = []
    
    relationships["Katrin Bach"] = ["Glebe Barn", "Eigg Primary School"] #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = ["Eigg Primary School"]
    
    relationships["Simon Helliwell"] = ["Glebe Barn"] #"Provide advice"
    relationships["Karen Helliwell"] = ["Glebe Barn"] 

    relationships["Louise Taylor"] = ["Eigg Primary School"]
    relationships["Martin Merrick"] = ["Eigg Primary School"]
    relationships["Kenneth Kean"] = ["Eigg Primary School"]
    relationships["Amanda Moult"] = ["Eigg Primary School"]
    relationships["Annabelle Scott-Moncrieff"] = ["Eigg Primary School"]
    relationships["Laraine Wyn-Jones"] = []
    relationships["Owain Wyn-Jones"] = []
    
    #SAME GUY?!?!?!?!!?!?!
    relationships["John Christopher Lynch"] = []
    relationships["John Christopher Clare"] = []
    relationships["John Booth"] = []
    
    relationships["George Carr"] = [] ##SHEEP FARMING
    relationships["Saira Renny"] = []
    
    relationships["Bob Wallace"] = ["Eigg Eco Centre"]
    
    relationships["Stuart Millar"] = ["Fishing Co"]
    
    relationships["Jenny Robertson"] = ["Eigg Crafts"]
    
    relationships["Donna McCulloch"] = ["Refuse Collection", "Eigg Crafts"] #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = []
    
    ##basket making
    relationships["Catherine Davies"] = ["Eigg Crafts"]
    relationships["Pascal Carr"] = ["Eigg Crafts"]
    
    relationships["Stuart Fergusson"] = []
    
    relationships["Peter Wade-Martins"] = []
    relationships["Susanna Wade-Martins"] = []
    
    relationships["Jacky"] = []
    relationships["Mick"] = []
    
    relationships["Mairi McKinnon"] = ["Health & Home Care"]
    relationships["Clare Miller"] = ["Health & Home Care"]
    
    relationships["John"] = []
    relationships["Sheila"] = [] #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = ["Eigg Crafts", "Eigg History"]
    relationships["Hilda Ibrahim"] = ["Eigg Crafts"]
    
    relationships["Ian Alexander James Bolas"] = []
    relationships["David Byres Newton"] = []
    relationships["Marc Allan Smith"] = []
    
    relationships["Jennifer Leiper"] = ["Clean Planet Now"]
    relationships["Robert Wallace"] = ["Clean Planet Now"]
    relationships["Rosemary Jane Acock"] = ["Clean Planet Now"]
    
    return relationships

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