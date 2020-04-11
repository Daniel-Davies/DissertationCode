
import networkx as nx
import multinetx as mx
from foodWebGraphing import *
from collections import defaultdict
import numpy as np
from utils import saveGraphToFile
import matplotlib.pyplot as plt
from anonymisationTools import *

def eiggEnvironmentalOrgs():
    # key organisations with power over environment
    ## 0 entries on the starting 2
    return ["Clean Planet Now", "Eigg Eco Centre", "Heritage Trust", "Eigg Electric", "Eigg Trading"]

def dependDirectlyOnNaturalResourcesRaw():
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

def dependDirectlyOnNaturalResources():
    rawData = dependDirectlyOnNaturalResourcesRaw()
    return anonymiseDataDict(rawData)

def getSpecificDependanciesFromEnvExtendedRaw():
    relationships = {} # will be FAMILY maps => aka needs to match first part of scientific name on Eigg data
    relationships['Alex Boden'] = ["poaceae"]     
    relationships['Sarah Boden'] = ["poaceae"]
    relationships['Elizabeth Boden'] = ["poaceae"]    
    relationships['Celia Bull'] = ["balaenopteridae", "phocidae", "phocoenidae", "delphinidae", "accipitridae", "sulidae", "laridae", "alcidae", "procellariidae", "scolopacidae", "anatidae", "passerellidae", "phalacrocoracidae"] 
    relationships['Eddie Scott'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "hedylidae", "hesperiidae", "lycaenidae", "papilionidae", "pieridae", "riodinidae"]
    relationships['Lucy Conway'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "hedylidae", "hesperiidae", "lycaenidae", "papilionidae", "pieridae", "riodinidae"]
    relationships['George Carr'] = ["poaceae"]
    relationships['Saira Renny'] = ["poaceae"]
    relationships['Laraine Wyn-Jones'] = ["phocidae", "accipitridae", "phocoenidae", "delphinidae", "balaenopteridae"]
    relationships['Owain Wyn-Jones'] = ["phocidae", "accipitridae", "phocoenidae", "delphinidae", "balaenopteridae"]
    relationships['Neil Robertson'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "hedylidae", "hesperiidae", "lycaenidae", "papilionidae", "pieridae", "riodinidae", "Meloidae", "Carabidae", "Chrysomelidae", "Silphidae", "Cantharidae", "Geotrupidae"]
    relationships['Sue Hollands'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "hedylidae", "hesperiidae", "lycaenidae", "papilionidae", "pieridae", "riodinidae", "Meloidae", "Carabidae", "Chrysomelidae", "Silphidae", "Cantharidae", "Geotrupidae"]
    relationships['Stuart Millar'] = ['Paralichthyidae', 'Gadidae']

    return relationships

def getSpecificDependanciesFromEnvExtended():
    rawData = getSpecificDependanciesFromEnvExtendedRaw()
    return anonymiseDataDict(rawData)

def getSpecificDependanciesFromEnvRaw():
        
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
    relationships['Celia Bull'] = ["balaenopteridae", "phocidae", "phocoenidae", "delphinidae", "accipitridae", "sulidae"] #https://www.tripadvisor.co.uk/Attraction_Review-g1898488-d10759115-Reviews-Selkie_Explorers-Isle_of_Eigg_The_Hebrides_Scotland.html

    #Many insects reap the benefits of bluebells which flower earlier than many other plants. all feed on their nectar. => https://www.woodlandtrust.org.uk/trees-woods-and-wildlife/plants/wild-flowers/bluebell/
    
    # FOR BUTTERFLIES => Reduce to families in North Europe Only (50 => 45) then 
    relationships['Eddie Scott'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "lycaenidae"]
    relationships['Lucy Conway'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "lycaenidae"]

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
    # Pollinators; removing beetles => https://www.thoughtco.com/insect-pollinators-that-arent-bees-or-butterflies-1967996
    # also beetles detroy plants => https://www.goodhousekeeping.com/home/gardening/a20705991/garden-insect-pests/, so assume guided pest control on them
    # except lady beetles => https://www.organiclesson.com/beneficial-insects-garden-pest-control/
    
    relationships['Neil Robertson'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "lycaenidae", "coccinellidae"]
    relationships['Sue Hollands'] = ["apidae", "vespidae", "syrphidae", "nymphalidae", "lycaenidae", "coccinellidae"]

    # species of typically consumable fish found in Eigg dataset [flounder, flatfish, cod]
    relationships['Stuart Millar'] = ['paralichthyidae', 'gadidae']

    return relationships

# FOOD FOR SELKIE IS LOCALLY SOURCED https://www.selkie-explorers.com/selkie-island-explorer-holidays/

def getSpecificDependanciesFromEnv():
    rawData = getSpecificDependanciesFromEnvRaw()
    return anonymiseDataDict(rawData)

def getEnvironmentallyInvolvedPeople():
    relationships = inferredNamesGraph()
    environmentalOrgs = dependDirectlyOnNaturalResources()

    dependanciesOnEnvironment = {}

    for item in relationships:
        if environmentalOrgs[item] == 1:
            dependanciesOnEnvironment[item] = relationships[item]

    return dependanciesOnEnvironment

def getEnumeratedJobsPerPersonRaw():
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

def getEnumeratedJobsPerPerson():
    rawData = getEnumeratedJobsPerPersonRaw()
    return anonymiseDataDict(rawData)

def buildEnvironmentCollaborationsGraph():
    nodes = getEnumeratedJobsPerPerson()
    environmentalOrgsOfInterst = set(eiggEnvironmentalOrgs())

    G = nx.Graph()
    labs = []
    for person in list(nodes.keys()): 
        labs.append(person)
        G.add_node(person)

    # clean for environmental nodes only

    for item in nodes:
        nodes[item] = list(set(nodes[item]).intersection(environmentalOrgsOfInterst))
    
    for person1 in nodes:
        for person2 in nodes:
            person1Orgs = set(nodes[person1])
            person2Orgs = set(nodes[person2])
            if person1 != person2 and len(list(person1Orgs.intersection(person2Orgs))) > 0:
                G.add_edge(person1,person2)
    
    return G, labs

def buildEnrichedFoodWeb(daterange=(2014,2021)):
    tempG,tempMapping = graphFoodWeb(dateRange=daterange)
    edgesToUseLater = tempG.edges()

    middleLayer = getSpecificDependanciesFromEnv()
    middleLayer = middleLayer.values()
    middleLayer = list(set([item.lower() for sublist in middleLayer for item in sublist]))
    
    G = nx.Graph()
    currNodeSet = set(G.nodes())
    additionSet = set()

    df = validatedEiggData()
    for family in middleLayer:
        translated = concreteSpeciesInterceptor(df,family)
        for concreteSpecies in translated:
            if concreteSpecies not in currNodeSet and concreteSpecies not in additionSet:
                additionSet.add(concreteSpecies)
    
    additionSet = list(additionSet)
    for item in additionSet:
        G.add_node(item)
    
    finalSet = set(G.nodes())
    for from_,to_ in edgesToUseLater:
        if from_ in finalSet and to_ in finalSet:
            G.add_edge(from_,to_)

    return G, additionSet

# https://goneoutdoors.com/types-of-grass-for-cattle-grazing-5011427.html
def concreteSpeciesInterceptor(df,family):
    if family == "poaceae": return ["phalaris arundinacea", "festuca rubra", "festuca arundinacea"]
    if family == "accipitridae": return ["haliaeetus albicilla", "aquila chrysaetos"]
    if family == "delphinidae": return ["delphinus delphis"]
    if family == "balaenopteridae": return ["balaenoptera acutorostrata"]
    return list(set(constrainByTaxonomy(df, ("Family", family))['Scientific name']))

def buildIntermediaryLayer():
    middleLayerLink = defaultdict(set)
    middleLayer = getSpecificDependanciesFromEnv()

    df = validatedEiggData()
    for name in middleLayer:
        dependencyFamilies = middleLayer[name]
        for family in dependencyFamilies:
            translated = concreteSpeciesInterceptor(df,family)
            for specificSpecies in translated:
                middleLayerLink[name].add(specificSpecies)
    
    for name in middleLayerLink:
        middleLayerLink[name] = list(middleLayerLink[name])

    return middleLayerLink

def buildMetaGraph(socialNodes, ecoNodes):
    M = np.zeros((len(socialNodes),len(ecoNodes)))    

    dependencies = getSpecificDependanciesFromEnv()

    for kp,person in enumerate(socialNodes):
        families = dependencies[person]
        for ke,e in enumerate(ecoNodes):
            concreteFamily = getTaxonomyForAnimal(e)["family"]
            M[kp,ke] = int(concreteFamily.lower() in families) 
    
    return M

def createEntireMetaNetExperiment(labels=False):
    Gs, labsS = buildEnvironmentCollaborationsGraph()
    Ge, labsE = buildEnrichedFoodWeb(daterange=(2010,2020))

    socialNodes = list(Gs.nodes())
    ecoNodes = list(Ge.nodes())

    M = buildMetaGraph(socialNodes,ecoNodes)

    if labels:
        return [(Gs,labsS), (Ge, labsE), M]
    else:
        return Gs,Ge,M

if __name__=="__main__":
    N = 30
    g1 = mx.erdos_renyi_graph(N,0.07,seed=218)
    g2 = mx.erdos_renyi_graph(N,0.0,seed=211)

    adj_block = mx.lil_matrix(np.zeros((N*2,N*2)))

    # adj_block = mx.lil_matrix(np.zeros((N*4,N*4)))


    adj_block[0:N, N:2*N] = np.random.poisson(0.009,size=(N,N))  # L_12
    adj_block += adj_block.T
    adj_block[adj_block>1] = 1


    mg = mx.MultilayerGraph(list_of_layers=[g1,g1], 
						inter_adjacency_matrix=adj_block)

    mg.set_edges_weights(inter_layer_edges_weight=100)

    mg.set_intra_edges_weights(layer=0,weight=30)
    mg.set_intra_edges_weights(layer=1,weight=30)

    fig = plt.figure(figsize=(15,5))
    ax1 = fig.add_subplot(121)

    ax2 = fig.add_subplot(122)
    ax2.axis('off')
    ax2.set_title('general multiplex network')
    pos = mx.get_position(mg,mx.fruchterman_reingold_layout(mg.get_layer(0)),
					  layer_vertical_shift=.3,
					  layer_horizontal_shift=0.9,
					  proj_angle=2)
    
    def colorMap(x):
        if x == 30:
            return 'green'
        
        return 'red'


    ecs = [mg[a][b]['weight'] for a,b in mg.edges()]
    ecs = list(map(lambda x: colorMap(x),ecs))
    mx.draw_networkx(mg,pos=pos,ax=ax2,node_size=40,with_labels=False,
				 edge_color=ecs,
				 edge_cmap=plt.cm.jet_r)
    print([mg[a][b]['weight'] for a,b in mg.edges()])
    plt.show()
