
import networkx as nx

def eiggEnvironmentalOrgs():
    # key organisations with power over environment
    return ["Clean Planet Now", "Eigg Eco Centre", "Heritage Trust", "Eigg Electric", "Eigg Trading"]

def dependDirectlyOnNaturalResources():
    relationships = {}

    # In other words
    # could I do this job in the centre of Bristol
    # Assumption; hotel businesses are not directly dependant
    
    relationships["Damian Helliwell"] = 0 # eigg crafts != directly dependant
    relationships["Margaret Fyffe"] = 0 
    relationships["Norah Barnes"] = 0
    relationships["Elizabeth Boden"] = 1 #yes- sandavore farm (sheep) depend on the environment to be healthy
    relationships["Lucy Conway"] = 1 # yes- depends on the bluebell production
    relationships["Sarah Boden"] = 1 # yes- oysters depend on the environment 
    relationships["Mark Alan Foxwell"] = 0
    relationships["Jacqueline Kirk"] = 0 #runs shop but this is technically not directly dependant on the environment
    relationships["Ian Leaver"] = 0
    relationships["Stuart McCarthy"] = 0 #supplies restaurants with beer 
    relationships["Tasha McVarish"] = 0
    
    relationships["Sue Hollands"] = 1 #eigg organics/ farming needs a healthy environment
    relationships["Neil Robertson"] = 1
    
    relationships["Sue Kirk"] = 0 #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = 0 ##INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = 0
    relationships["Libby Galli"] = 0
    
    relationships["Eddie Scott"] = 1 #eddies eigg croft needs a healthy environment to grow bluebells
    
    relationships["Marie Carr"] = 0
    relationships["Colin Carr"] = 0
    relationships["Greg Carr"] = 0
    
    relationships["Alex Boden"] = 1 #sandavore farm needs a healthy environment
    
    relationships["Katrin Bach"] = 0 #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = 0
    
    relationships["Simon Helliwell"] = 0 #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = 0 #daughter is now technically owner

    relationships["Louise Taylor"] = 0
    relationships["Martin Merrick"] = 0
    relationships["Kenneth Kean"] = 0
    relationships["Amanda Moult"] = 0
    relationships["Annabelle Scott-Moncrieff"] = 0
    relationships["Laraine Wyn-Jones"] = 1 #yes- sightseeing industry
    relationships["Owain Wyn-Jones"] = 1 #yes- sightseeing industry
    
    #SAME GUY?!?!?!?!!?!?!
    relationships["John Christopher Lynch"] = 0
    relationships["John Christopher Clare"] = 0
    relationships["John Booth"] = 0
    
    relationships["George Carr"] = 1 #yes- farm needs good environment
    relationships["Saira Renny"] = 1 #yes- farm needs good environment
    
    relationships["Bob Wallace"] = 0
    
    relationships["Stuart Millar"] = 1 #yes- inherently, he is a fisherman
    
    relationships["Jenny Robertson"] = 0
    
    relationships["Donna McCulloch"] = 0 #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = 1 #yes- directly involved in the sightseeing industry
    
    ##basket making
    relationships["Catherine Davies"] = 0
    relationships["Pascal Carr"] = 0
    
    relationships["Stuart Fergusson"] = 0
    
    relationships["Peter Wade-Martins"] = 0
    relationships["Susanna Wade-Martins"] = 0
    
    relationships["Jacky"] = 0
    relationships["Mick"] = 0
    
    relationships["Mairi McKinnon"] = 0
    relationships["Clare Miller"] = 0
    
    relationships["John"] = 0
    relationships["Sheila"] = 0 #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = 0
    relationships["Hilda Ibrahim"] = 0
    
    relationships["Ian Alexander James Bolas"] = 0
    relationships["David Byres Newton"] = 0
    relationships["Marc Allan Smith"] = 0
    
    relationships["Jennifer Leiper"] = 0
    relationships["Robert Wallace"] = 0
    relationships["Rosemary Jane Acock"] = 0
    
    return relationships

def getSpecificDependanciesFromEnv():
        
    # relationships["Heritage Trust"] = []
    # relationships["Clean Planet Now"] = []
    # relationships["Eigg Electric"] = [] # EVERYONE?!
    # relationships["Eigg Eco Centre"] = []
    # relationships["Eddie's Eigg Croft"] = [] 
    # relationships["Eigg Organics"] = []
    # relationships["Eigg Adventures"] = []
    # relationships["Eigg Camping Pods"] = []
    
    relationships = {} # will be FAMILY maps => aka needs to match first part of scientific name on Eigg data
    # any kinds of grass
    relationships['Alex Boden'] = ["poaceae"]     
    relationships['Sarah Boden'] = ["poaceae"]
    relationships['Elizabeth Boden'] = ["poaceae"]
    
                                # [Minkie Whale, seals, porpoise, dolphin, naval eagle, gannets&fish predators, ...sea birds]
    relationships['Celia Bull'] = ["balaenopteridae", "phocidae", "phocoenidae", "delphinidae", "accipitridae", "sulidae", "laridae", "alcidae", "procellariidae", "scolopacidae", "anatidae", "passerellidae", "phalacrocoracidae"] #https://www.tripadvisor.co.uk/Attraction_Review-g1898488-d10759115-Reviews-Selkie_Explorers-Isle_of_Eigg_The_Hebrides_Scotland.html

    #Many insects reap the benefits of bluebells which flower earlier than many other plants. all feed on their nectar. => https://www.woodlandtrust.org.uk/trees-woods-and-wildlife/plants/wild-flowers/bluebell/
    relationships['Eddie Scott'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "hedylidae", "hesperiidae", "lycaenidae", "papilionidae", "pieridae", "riodinidae"]
    relationships['Lucy Conway'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "hedylidae", "hesperiidae", "lycaenidae", "papilionidae", "pieridae", "riodinidae"]

    # any kinds of grass
    relationships['George Carr'] = ["poaceae"]
    relationships['Saira Renny'] = ["poaceae"]

    # seals => http://www.eiggadventures.co.uk/isle-of-eigg-trail-running-camp/
    # gold or white tailed eagles => http://www.eiggadventures.co.uk/bike-hire-on-eigg/
    # otters, sea eagles, porpoise, dolphins and minke whales  => http://www.eiggadventures.co.uk/kayaking-on-eigg/
    relationships['Laraine Wyn-Jones'] = ["phocidae", "accipitridae", "phocoenidae", "delphinidae", "balaenopteridae"]
    relationships['Owain Wyn-Jones'] = ["phocidae", "accipitridae", "phocoenidae", "delphinidae", "balaenopteridae"]

    # pollinators, protective insects for plants?
    # pollinators => https://scottishpollinators.wordpress.com/2018/08/31/pollinators-in-scotland/
    # pollinators => https://www.youtube.com/watch?v=_HdHLsLAb-k
    relationships['Neil Robertson'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "hedylidae", "hesperiidae", "lycaenidae", "papilionidae", "pieridae", "riodinidae", "Meloidae", "Carabidae", "Chrysomelidae", "Silphidae", "Cantharidae", "Geotrupidae"]
    relationships['Sue Hollands'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "hedylidae", "hesperiidae", "lycaenidae", "papilionidae", "pieridae", "riodinidae", "Meloidae", "Carabidae", "Chrysomelidae", "Silphidae", "Cantharidae", "Geotrupidae"]

    # species of typically consumable fish found in Eigg dataset [flounder, flatfish, cod]
    relationships['Stuart Millar'] = ['Paralichthyidae', 'Gadidae']

    return relationships

# FOOD FOR SELKIE IS LOCALLY SOURCED https://www.selkie-explorers.com/selkie-island-explorer-holidays/

def getEnvironmentallyInvolvedPeople():
    relationships = inferredNamesGraph()
    environmentalOrgs = dependDirectlyOnNaturalResources()

    dependanciesOnEnvironment = {}

    for item in relationships:
        if environmentalOrgs[item] == 1:
            dependanciesOnEnvironment[item] = relationships[item]

    return dependanciesOnEnvironment

def getEnumeratedJobsPerPerson():
    relationships = {}
    
    relationships['Alex Boden'] = ["Eigg Shed", "Sandavore Farm", "Eigg Huts", "Hebnet Cic"] 
    relationships['Celia Bull'] = ["Selkie Explorers"] 
    relationships['Eddie Scott'] = ["Sweeney's Bothy","Eddie's Eigg Croft",'Eigg Electric','Eigg Shop']
    relationships['Elizabeth Boden'] = ['Eigg Huts','Heritage Trust','Eigg Shed','Eigg Primary School','Sandavore Farm','Eigg Trading']
    relationships['George Carr'] = ['Laig Farm', 'Eigg Shop']
    relationships['Laraine Wyn-Jones'] = ['Eigg Adventures', 'Eigg Camping Pods', 'Eigg Trading']
    relationships['Lucy Conway'] = ['Heritage Trust','Lagerona',"Sweeney's Bothy","Eddie's Eigg Croft",'Eigg Primary School','Eigg Shop']
    relationships['Neil Robertson'] = ['Eigg Organics', 'Roadworks']
    relationships['Owain Wyn-Jones'] = ['Eigg Adventures', 'Eigg Camping Pods']
    relationships['Saira Renny'] = ['Laig Farm', 'Eigg Shop']
    relationships['Sarah Boden'] = ['Eigg Huts','Heritage Trust','Eigg Electric','Sandavore Farm','Kildonnan Bay Oysters']
    relationships['Stuart Millar'] = ['Fishing Co', 'Galmisdale Cafe', 'Lagerona']
    relationships['Sue Hollands'] = ['Eigg Organics', 'Eigg Electric']

    return relationships

def buildEnvironmentCollaborationsGraph():
    nodes = getEnumeratedJobsPerPerson()
    environmentalOrgsOfInterst = set(eiggEnvironmentalOrgs())

    G = nx.Graph()
    for person in list(nodes.keys()): G.add_node(person)

    # clean for environmental nodes only

    for item in nodes:
        nodes[item] = list(set(nodes[item]).intersection(environmentalOrgsOfInterst))
    
    for person1 in nodes:
        for person2 in nodes:
            person1Orgs = set(nodes[person1])
            person2Orgs = set(nodes[person2])
            if person1 != person2 and len(list(person1Orgs.intersection(person2Orgs))) > 0:
                G.add_edge(person1,person2)
    
    return G 