
import networkx as nx
# import multinetx as mx
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

def dependDirectlyOnNaturalResources():
    return accessAnonymisedDataDict('dependDirectlyOnNaturalResourcesRaw')

def getSpecificDependanciesFromEnvExtended():
    return accessAnonymisedDataDict('getSpecificDependanciesFromEnvExtendedRaw')

def getSpecificDependanciesFromEnv():
    return accessAnonymisedDataDict('getSpecificDependanciesFromEnvRaw')

def getEnvironmentallyInvolvedPeople():
    relationships = inferredNamesGraph()
    environmentalOrgs = dependDirectlyOnNaturalResources()

    dependanciesOnEnvironment = {}

    for item in relationships:
        if environmentalOrgs[item] == 1:
            dependanciesOnEnvironment[item] = relationships[item]

    return dependanciesOnEnvironment

def getEnumeratedJobsPerPerson():
    return accessAnonymisedDataDict('getEnumeratedJobsPerPersonRaw')

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
