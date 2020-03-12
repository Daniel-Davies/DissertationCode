from math import sin, cos, sqrt, atan2, radians
import networkx as nx
import numpy as np
from math import sin, cos, sqrt, atan2, radians,pi
import json

def graphASetByObservations(buildings,dist=500):
    G = nx.Graph()
    for k,r in enumerate(buildings):
        G.add_node(k)

    for o_index,o in enumerate(buildings):
        for r_index,r in enumerate(buildings):
            if o_index != r_index:
                if seperationInMetres(o,r) < dist:
                    G.add_edge(o_index,r_index)
                
    return G


def transformLatLonByXMetres(lat,lon,dn,de):
    R=6378137
    dLat = dn/R
    dLon = de/(R*cos(pi*lat/180))
    latO = lat + dLat * 180/pi
    lonO = lon + dLon * 180/pi

    return (latO,lonO)

# technically doesnt count the fact the earth isnt a sphere
def seperationInMetres(p1,p2):
    R = 6373.0
    lat1,lon1 = p1
    lat2, lon2 = p2
    
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    #convert to metres
    return distance * 1000

def outputGraphToFile(G,filename):
    f = nx.to_numpy_matrix(G)
    np.savetxt(filename, f, "%d")  

def latLonToString():
    return ",".join([str(x[0]),str(x[1])])

def toUsableLatLon(coord):
    lst = coord.split(",")
    return list(map(lambda x: float(x), lst))

def toUsableLatLonList(coords):
    return list(map(lambda x: toUsableLatLon(x),coords))

def saveGraphToFile(G, filename):
    file_ = nx.to_numpy_matrix(G)
    print(file_.shape)
    print()
    np.savetxt(filename,file_, "%d")  

def constrainRecordsToDateRange(df,dateRangeTuple):
    from_,to_ = dateRangeTuple
    return df[(df['End date year'] < to_) & (df['Start date year'] >= from_)]

#markingTuples => (icon,data[]) OR (icon, data[], labels[])
def generateMapJSON(markingTuples,graphTuples,filename):
    building = {}
    building["result"] = {}

    for k,item in enumerate(markingTuples):
        if len(item) == 1:
            markingTuples[k] = ('./fullColMarkers/marker76.png',item[0],[""]*len(item[0]),[0.03]*len(item[0]))
        elif len(item) == 2:
            markingTuples[k] = (item[0],item[1],[""]*len(item[1]),[0.03]*len(item[1]))
        elif len(item) == 3:
            markingTuples[k] = (item[0],item[1],item[2],[0.03]*len(item[1]))
    
    markersToDraw = []
    # markerIcon => "./X.png" aka a valid path
    # markerData => [[56.12343,-6.232234], [56.423423,-6.4324]] 
    for (markerIcon, markerLocs, markerLabels, markerSizes) in markingTuples:
        dict_ = {}
        dict_["marker"] = markerIcon
        
        dict_["points"] = list(map(lambda x: {"location": x[1], "size":markerSizes[x[0]], "desc":markerLabels[x[0]]},enumerate(markerLocs)))
        markersToDraw.append(dict_)
    
    building["result"]["plots"] = markersToDraw

    for k,item in enumerate(graphTuples):
        if len(item) == 2:
            graphTuples[k] = ("#FF0000",item[0],item[1])
    
    lineLayers = []
    # coords can be whatever as long as they are keyed by the Graph edges
    # key => [[56.21324,-6.143242]...]
    for (lineColor, coords, G) in graphTuples:
        dict_ = {}
        dict_["lineColor"] = lineColor
        dict_["lines"] = list(map(lambda x: [coords[x[0]],coords[x[1]]],G.edges()))

        lineLayers.append(dict_)
    
    building["result"]["lines"] = lineLayers
    
    with open(filename, "a") as f:
        f.write(json.dumps(building))
    