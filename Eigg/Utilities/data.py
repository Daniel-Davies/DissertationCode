import pandas as pd
import numpy as np
import pickle
# CONTAINS DICTIONARIES OF DOUBLE CHECKED LAT/LON POINTS PER OBS

basedir = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/Utilities/"
islandDatasets = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/IslandDatasets/"

def listedEiggHotels():
    hotels = {}
    hotels['56.9214209,-6.1472527'] = "Tigh an Sithean – camping cabins & log cabins"
    hotels['56.9195159,-6.1484787'] = "Lageorna"
    hotels['56.9252864,-6.1471206'] = "Tophouse"
    hotels['56.888082, -6.137512'] = "Amazing Eigg Shed" #ref, Airbnb https://www.airbnb.co.uk/rooms/16893915?source_impression_id=p3_1582112234_GzrTX7%2FlFXGr%2FdFV
    hotels['56.922044,-6.1446842'] = "Eigg Organics"
    hotels['56.8889489,-6.1250917'] = "Kildonnan house" 
    hotels['56.9182625,-6.1554283'] = "Laig Caravan"
    hotels['56.8902145,-6.1343823'] = "Glebe Barn"
    hotels['56.8775889,-6.1337773'] = "The Smiddy"
    hotels['56.9222615,-6.1420233'] = "Sweeney's Bothy"
    hotels['56.9131675,-6.1619473'] = "Laig Beach Bothy"
    hotels['56.8779645,-6.1327783'] = "Eigg Camping Pods"
    hotels['56.9223021,-6.1480099'] = "Tigh Eilidh"
    hotels['56.8804676,-6.1417635'] = "Eigg Eco Centre"
    hotels['56.8777055,-6.1316373'] = "Clanranald college"
    hotels['56.9269519,-6.1439637'] = "Howlin Cottege"
    hotels['56.9017079,-6.1425028'] = "Cuagath Bothy"

    return hotels

def inferredBusinessLocations():
    locs = {}
    ## UNKNOWN LOCATION: Default to the heritage centre
    locs['Heritage Trust'] = '56.9023849,-6.1449937'
    locs['Clean Planet Now'] = '56.8806589,-6.1399077'
    locs['Eigg Electric'] = '56.9023849,-6.1449937'
    locs['Eigg Trading'] = '56.9023849,-6.1449937'
    locs['Eigg Construction'] = '56.9023849,-6.1449937'
    locs['The Bothy Cuagach'] = '56.9017079,-6.1425028'
    locs['Eigg Eco Centre'] = '56.8806589,-6.1399077'
    locs['Eigg Huts'] = '56.9023849,-6.1449937' #https://addressesandpostcodes.co.uk/address/ch-Kq5bssfX/eigg-huts-ltd-sandavor-house-sandavor-house-isle-of-eigg-ph42-4rl-ph42-4rl.html
    locs['Eigg Shed'] = '56.888082, -6.137512'
    locs['Eigg Primary School'] = '56.8995521,-6.1420288'
    locs['Sandavore Farm'] = '56.8849159,-6.1415287'
    locs['Lagerona'] = '56.9195159,-6.1484787'
    locs["Sweeney's Bothy"] = '56.9222615,-6.1420233'
    locs["Eddie's Eigg Croft"] = '56.9222615,-6.1420233'
    locs['Eigg Shop'] = '56.8773467,-6.1308262'
    locs['Kildonnan Bay Oysters'] = '56.9023849,-6.1449937'
    locs['Glebe Barn'] = '56.8902145,-6.1343823'
    locs['Laig Bay Brewing'] = '56.8902145,-6.1343823'
    locs['Galmisdale Cafe'] = '56.8773467,-6.1308262'
    locs['Equilibrium Eigg Massage Therapy'] = '56.9023849,-6.1449937'
    locs['Eigg Organics'] = '56.922044,-6.1446842'
    locs['Roadworks'] = '56.922044,-6.1446842' #where he lives
    locs['Kildonnan'] = '56.8889489,-6.1250917'
    locs['Taxi Service'] = '56.9023849,-6.1449937'
    locs['Eigg Crafts'] = '56.8772127,-6.1312982'
    locs['Kildonnan House'] = '56.8889489,-6.1250917'
    locs['Hebnet Cic'] = '56.9023849,-6.1449937'
    locs['Eiggy Bread'] = '56.9023849,-6.1449937'
    locs['Eigg Adventures'] = '56.8773155,-6.1319773'
    locs['Eigg Camping Pods'] = '56.8779645,-6.1327783'
    locs['LOST MAPS RECORDS LTD'] = '56.8995081,-6.1392071'
    locs['Laig Farm'] = '56.9131675,-6.1619473'
    locs['Fishing Co'] = '56.9269519,-6.1439637' #=howling http://news.bbc.co.uk/1/hi/scotland/highlands_and_islands/6748779.stm
    locs['A NEAD KNITWEAR'] = '56.9016979,-6.1441872'
    locs['Refuse Collection'] = '56.9023849,-6.1449937'
    locs['Selkie Explorers'] = '56.8771649,-6.1323427'
    locs['Tophouse'] = '56.9249419,-6.1493057'
    locs['TIGH AN SITHEAN'] = '56.9214209,-6.1472527'
    locs['Health & Home Care'] = '56.9023849,-6.1449937'
    locs['Eigg Yurts'] = '56.9208039,-6.1455767'
    locs['Craigard Teas'] = '56.8772749,-6.1348967'
    locs['Eigg History'] = '56.9023849,-6.1449937'
   
    return locs

def electricGrid():
    electrics = {}
    electrics['56.909761,-6.163664'] = "Laig Hydro"
    electrics['56.888556,-6.122431'] = "Kildonan Hydro"
    electrics['56.878528,-6.132869'] = "Pier Hydro"
    
    electrics['56.876541,-6.145949'] = "Turbines"
    
    electrics['56.887181,-6.138750'] = "PV Panels"    
    electrics['56.888083,-6.137484'] = "Generator"
        
    electrics['56.8769979,-6.1536679'] = "Turbine" #turbines
    electrics['56.8765690,-6.1531231'] = "Turbine"
    electrics['56.8767902,-6.1533662'] = "Turbine"
    electrics['56.8764323,-6.1527857'] = "Turbine"
    
    electrics['56.8769979,-6.1536679'] = "Generator" #generators
    electrics['56.8765690,-6.1531231'] = "Generator"
    electrics['56.8767902,-6.1533662'] = "Generator"
    electrics['56.8764323,-6.1527857'] = "Generator"
    
    return electrics

## Residences locations
def pointsOfInterest():
    interests = {}
    interests['56.8781465,-6.1326085'] = "historic memorial"
    interests['56.9003152,-6.1404042'] = "historic monument"
    interests['56.9199238,-6.1467235'] = "historic memorial"
    
    interests['56.8797535,-6.1267920'] = "ferry_terminal"
    interests['56.9190886,-6.1463398'] = "restaurant"        
    interests['56.8798083,-6.1462677'] = "Town Hall"
    interests['56.8932164,-6.1448756'] = "Church"
    interests['56.9025486,-6.1389638'] = "Primary School"
    interests['56.9031345,-6.1392428'] = "Heritage Trust"
    interests['56.917479,-6.1453462'] = "Roman Church"
    interests['56.8802725,-6.1417391'] = "Eco Center"
    interests['56.901693,-6.141992'] = "Old Museum"
    interests['56.9199238,-6.1467235'] = 'Eigg War Memorial'
    interests['56.8709333,-6.1213667'] = "lighthouse"
    
    #naturals
    
    interests['56.8840899,-6.1652639'] = "Peak"
    interests['56.8736995,-6.1455634'] = "Cave Entrance"
    interests['56.8735485,-6.1499874'] = "Cave Entrance"
    interests['56.9187381,-6.1651365'] = "Bay"
    interests['56.9264321,-6.1333792'] = "Peak"
    interests['56.8693995,-6.1271392'] = "Peak"
    interests['56.9034271,-6.1912247'] = "Peak"
    interests['56.9136453,-6.1311475'] = "Peak"
    interests['56.8911480,-6.1761228'] = "Peak"
    interests['56.8794302,-6.1776533'] = "Grulin"
    interests['56.8840899,-6.1652639'] = "An Sgurr"
    interests['56.8736995,-6.1455634'] = "Massacre Caves"
    interests['56.9187381,-6.1651365'] = "Laig Bay"
    interests['56.8781465,-6.1326085'] = "Sgurr Stone"
    interests['56.9264321,-6.1333792'] = "Sgorr an Fharaidh"
    interests['56.8693995,-6.1271392'] = "Maol an Eilean"
    interests['56.9034271,-6.1912247'] = "Beinn Tighe"
    interests['56.9136453,-6.1311475'] = "Beinn Tighe"
    interests['56.8911480,-6.1761228'] = "Cora Bheinn"
    
    return interests

def residentialEntry():
    
    residentials = {}

    residentials['56.9192255,-6.1462968'] = "lageorona site"    
    residentials['56.9218827,-6.1464040'] = "cleadale"
    residentials['56.8888173,-6.1227537'] = "kildonnan"
    residentials['56.8770948,-6.1389645'] = "Galmisdale"
    residentials['56.9285566,-6.1433419'] = "Howlin"
    residentials['56.8794302,-6.1776533'] = "Grulin"
    residentials['56.9190886,-6.1463398'] = 'Lageorna'
    
    residentials['56.9199238,-6.1467235'] = 'Eigg War Memorial'
    residentials['56.9218827,-6.1464040'] = '<village>'
    residentials['56.8888173,-6.1227537'] = '<locality>'
    residentials['56.8757409,-6.1392217'] = 'locality'
    residentials['56.9285566,-6.1433419'] = '<village>'
    residentials['56.8794302,-6.1776533'] = '<locality>'
    residentials['56.8802725,-6.1417391'] = "Eco Center"
    
    residentials['56.9018832,-6.1449375'] ="1 Cuagach"
    residentials['56.907887,-6.1960333'] ="2 Cuagach"
    residentials['56.9018832,-6.1449375'] ="2 New House, Cleadale"
    residentials['56.9018832,-6.1449375'] ="3 Cuagach"
    residentials['56.9018832,-6.1449375'] ="3 New House, Cleadale"
    residentials['56.9018832,-6.1449375'] ="4 Cleadale"
    residentials['56.9018832,-6.1449375'] ="4 New House, Cleadale"
    residentials['56.9018832,-6.1449375'] ="5 Cleadale"
    residentials['56.9018832,-6.1449375'] ="6 Cleadale"
    residentials['56.9018832,-6.1449375'] ="6 New House, Cleadale"
    residentials['56.901837, -6.120534'] ="Brae Cottage"

    residentials['56.8804647,-6.1417635'] ="Earth Connections Sustainability Centre"
    residentials['56.902125, -6.142966'] ="Foresters Cottage"
    residentials['56.878903, -6.146895'] ="Galmisdale House"
    residentials['56.9272042,-6.1444563'] ="Howlin Cottage"
    residentials['56.928432, -6.144725'] ="Howlin House"
    residentials['56.888946,-6.1250917'] ="Kildonan House"
    residentials['56.9194645,-6.1463873'] ="Lageorna"
    residentials['56.911597, -6.161675'] ="Laig Farm"
    residentials['56.877696, -6.130619'] ="Millers Cottage"
    residentials['56.8778748,-6.1306834'] ="Pier Cottage"
    residentials['56.9031345,-6.1392428'] ="Sandamhor Bothy"
    residentials['56.9031345,-6.1392428'] ="Sandamhor Farm"
    residentials['56.9243404,-6.1522132'] ="Seaview"
    residentials['56.918268, -6.154348'] ="Shore Cottage"
    residentials['56.877586,-6.1370604'] ="Smithy"
    residentials['56.877586,-6.1370604'] ="The Bothy Cuagach"
    residentials['56.917893, -6.147771'] ="The Crows Nest" 
    residentials['56.890261,-6.1341621'] ="The Glebe"
    residentials['56.889429, -6.135299'] ="The Manse"

    residentials['56.9222992,-6.1458212'] = "Tigh Eilidh"
    residentials['56.921928, -6.146227'] ="Tigh A Bhlar"
    residentials['56.921726, -6.145699'] ="Tigh An Sithean"
    residentials['56.921563, -6.145661'] ="Tigh An Tobar, Cleadale"
    residentials['56.921408, -6.145718'] ="Tigh Sandabheag"
    residentials['56.9249419,-6.1493057'] ="Top House, Cleadale"
    
    return residentials

def uninferredNamesGraph():
    relationships = {}
    
    relationships["Damian Helliwell"] = ["Heritage Trust", "Eigg Crafts"]
    relationships["Margaret Fyffe"] = ["Clean Planet Now", "Heritage Trust", "Eigg Electric", "Eigg Trading", "Eigg Construction", "The Bothy Cuagach"]
    relationships["Norah Barnes"] = ["Clean Planet Now", "Heritage Trust", "Eigg Eco Centre"]
    relationships["Elizabeth Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Shed", "Eigg Primary School", "Sandavore Farm", "Eigg Trading"]
    relationships["Lucy Conway"] = ["Heritage Trust", "Lagerona", "Sweeney's Bothy", "Eddie's Eigg Croft", "Eigg Primary School"] #accountant, wife to eddie
    relationships["Sarah Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Electric", "Sandavore Farm", "Kildonnan Bay Oysters"]
    relationships["Mark Alan Foxwell"] = ["Heritage Trust"]
    relationships["Jacqueline Kirk"] = ["Heritage Trust", "Eigg Shop"]
    relationships["Ian Leaver"] = ["Heritage Trust"]
    relationships["Stuart McCarthy"] = ["Glebe Barn","Heritage Trust", "Laig Bay Brewing", "Galmisdale Cafe", "Lagerona", "Eigg Construction"] #supplies restaurants with beer 
    relationships["Tasha McVarish"] = ["Heritage Trust", "Eigg Primary School", "Equilibrium Eigg Massage Therapy"]
    
    relationships["Sue Hollands"] = ["Eigg Organics", "Eigg Electric"]
    relationships["Neil Robertson"] = ["Eigg Organics", "Roadworks"]
    
    relationships["Sue Kirk"] = ["Lagerona", "Kildonnan House", "Eigg Shop", "Eigg Construction"] #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = ["Lagerona", "Eigg Construction"] ##INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = ["Taxi Service"]
    relationships["Libby Galli"] = ["Eigg Crafts"]
    
    relationships["Eddie Scott"] = ["Sweeney's Bothy", "Eddie's Eigg Croft", "Eigg Electric"]
    
    relationships["Marie Carr"] = ["Kildonnan House"]
    relationships["Colin Carr"] = ["Kildonnan House", "Eigg Electric", "Eigg Construction"]
    relationships["Greg Carr"] = ["Kildonnan House", "Eigg Trading"]
    
    relationships["Alex Boden"] = ["Eigg Shed", "Sandavore Farm", "Eigg Huts", "Hebnet Cic"]
    
    relationships["Katrin Bach"] = ["Eiggy Bread", "Glebe Barn", "Eigg Primary School"] #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = ["Glebe Barn", "Eigg Primary School", "Eigg Construction"]
    
    relationships["Simon Helliwell"] = ["Glebe Barn", "Hebnet Cic"] #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = ["Glebe Barn"] #daughter is now technically owner

    relationships["Louise Taylor"] = ["Eigg Primary School"]
    relationships["Martin Merrick"] = ["Eigg Primary School"]
    relationships["Kenneth Kean"] = ["Eigg Primary School"]
    relationships["Amanda Moult"] = ["Eigg Primary School"]
    relationships["Annabelle Scott-Moncrieff"] = ["Eigg Primary School"]
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
    
    relationships["Jenny Robertson"] = ["A NEAD KNITWEAR", "Eigg Crafts"]
    
    relationships["Donna McCulloch"] = ["Refuse Collection", "Eigg Crafts"] #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = ["Selkie Explorers"]
    
    ##basket making
    relationships["Catherine Davies"] = ["Eigg Crafts"]
    relationships["Pascal Carr"] = ["Eigg Crafts"]
    
    relationships["Stuart Fergusson"] = ["Eigg Trading", "Galmisdale Cafe"]
    
    relationships["Peter Wade-Martins"] = ["Tophouse"]
    relationships["Susanna Wade-Martins"] = ["Tophouse"]
    
    relationships["Jacky"] = ["TIGH AN SITHEAN"]
    relationships["Mick"] = ["TIGH AN SITHEAN"]
    
    relationships["Mairi McKinnon"] = ["Health & Home Care"]
    relationships["Clare Miller"] = ["Health & Home Care", "Eigg Yurts"]
    
    relationships["John"] = ["Craigard Teas"]
    relationships["Sheila"] = ["Craigard Teas"] #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = ["Eigg Crafts", "Eigg History"]
    relationships["Hilda Ibrahim"] = ["Eigg Crafts"]
    
    relationships["Ian Alexander James Bolas"] = ["Hebnet Cic"]
    relationships["David Byres Newton"] = ["Hebnet Cic"]
    relationships["Marc Allan Smith"] = ["Hebnet Cic"]
    
    relationships["Jennifer Leiper"] = ["Clean Planet Now"]
    relationships["Robert Wallace"] = ["Clean Planet Now"]
    relationships["Rosemary Jane Acock"] = ["Clean Planet Now"]
    
    return relationships

def allBusinessNames():
    relationships = {}

    relationships["Heritage Trust"] = []
    relationships["Eigg Crafts"] = []
    relationships["Clean Planet Now"] = []
    relationships["Eigg Electric"] = [] # EVERYONE?!
    relationships["Eigg Trading"] = []
    relationships["Eigg Construction"] = []
    relationships["The Bothy Cuagach"] = []
    relationships["Eigg Eco Centre"] = []
    relationships["Eigg Huts"] = []
    relationships["Eigg Shed"] = []
    relationships["Sandavore Farm"] = []
    relationships["Lagerona"] = []
    relationships["Sweeney's Bothy"] = []
    relationships["Eddie's Eigg Croft"] = [] 
    relationships["Kildonnan Bay Oysters"] = []
    relationships["Eigg Shop"] = []
    relationships["Glebe Barn"] = []
    relationships["Laig Bay Brewing"] = []
    relationships["Galmisdale Cafe"] = []
    relationships["Equilibrium Eigg Massage Therapy"] = []
    relationships["Eigg Organics"] = []
    relationships["Kildonnan House"] = []
    relationships["Hebnet Cic"] = []
    relationships["Eiggy Bread"] = []
    relationships["Eigg Adventures"] = []
    relationships["Eigg Camping Pods"] = []
    relationships["A Nead Knitwear"] = []
    relationships["Eigg Yurts"] = []
    relationships["Eigg History"] = []
    relationships["Craigard Teas"] = []

    return list(set(relationships.keys()) - set(["Equilibrium Eigg Massage Therapy", "Eigg Adventures", "Eddie's Eigg Croft"]))


# A LIST OF ALL POSSIBLE INTERACTIONS BY BUSINESSES
# AKA MANUALLY INPUT, NOT INFERRED BY THE EMPLOYEES
def customByBusiness():
    relationships = {}
    #heritage trust + subsidiaries => http://isleofeigg.org/ieht/
    #Beer in the shop => https://isleofeiggshop.com/our-stock/

    #subsidiary or interaction

    # INFERENCES LIST

    # Sandavore Farm => Lamb => Eigg Shop, Galmisdale Cafe, Lagerona

    # rigg eco centre promoting/ somehow involved in clean planet now => http://www.earthconnections.co.uk/
    # Eigg organics provides meals to eco centre http://www.earthconnections.co.uk/

    #iheritance on shop: Eigg Organics/ crofters => EIgg Shop => Lagerona/Eigg Bread ...

    relationships["Heritage Trust"] = ["Eigg Electric", "Eigg Construction", "Eigg Trading", "Small Isles Medical Centre"]
    relationships["Eigg Crafts"] = ["A Nead Knitwear", "Eddie's Eigg Croft"]
    relationships["Clean Planet Now"] = []
    relationships["Eigg Electric"] = []#allBusinessNames() # EVERYONE?!
    relationships["Eigg Trading"] = ["Eigg Shop", "Craigard Teas", "Eigg Crafts"]    
    relationships["Eigg Construction"] = ["Eigg Trading"] #no evidence for anything apart from "5 (undocumented) refurbishments" - IEHT.com
    relationships["The Bothy Cuagach"] = [] #nothing documented
    relationships["Eigg Eco Centre"] = ["Eigg Shop", "Clean Planet Now"] #dining so involved with Eigg Organics lets say for means, and Eigg Shop to plug gap
    relationships["Eigg Huts"] = ["Eigg Shed", "Sweeney's Bothy"]
    relationships["Eigg Shed"] = ["Sweeney's Bothy"]
    relationships["Sandavore Farm"] = ["Eigg Shop", "Galmisdale Cafe", "Lagerona"]
    relationships["Lagerona"] = ["Kildonnan House"]
    relationships["Sweeney's Bothy"] = ["Eigg Shed"]
    relationships["Eddie's Eigg Croft"] = [] #bluebell seeds only really 
    relationships["Kildonnan Bay Oysters"] = ["Lagerona", "Galmisdale Cafe"] #lets say they supply the restaurants 
    relationships["Eigg Shop"] = ["Galmisdale Cafe", "Lagerona"] #send nonlocal supplies to the restaurants [INCLUDE EVERYONE?]
    relationships["Glebe Barn"] = [] #no special interactions documented
    relationships["Laig Bay Brewing"] = ["Galmisdale Cafe", "Lagerona", "Eigg Shop"]
    relationships["Galmisdale Cafe"] = [] #nothing out of the ordinary/ undocumented added
    relationships["Equilibrium Eigg Massage Therapy"] = ["Small Isles Medical Centre"] # https://eiggmassagetherapy.wordpress.com/about/
    relationships["Eigg Organics"] = ["Eigg Eco Centre", "Eigg Shop", "Lagerona"]
    relationships["Kildonnan House"] = [] #nothing out of the ordinary documenteds
    relationships["Hebnet Cic"] = ["Lagerona", "Glebe Barn", "Kildonnan House"] #EVERYONE?
    relationships["Eiggy Bread"] = ["Glebe Barn", "Eigg Shop"] #provide the catering them, suppose thye get ingredients from the shop
    relationships["Eigg Adventures"] = []  
    relationships["Eigg Camping Pods"] = []
    relationships["A Nead Knitwear"] = []
    relationships["Eigg Yurts"] = []
    relationships["Eigg History"] = []
    relationships["Craigard Teas"] = ["Eigg Shop"]
    
    return relationships

def inferredNamesGraph():
    relationships = uninferredNamesGraph()
    
    #Own a sheep farm ("Laig Farm") 
    # => Supply Eigg Shop with fresh lamb [heraldscott article]
    relationships["George Carr"].append("Eigg Shop")
    relationships["Saira Renny"].append("Eigg Shop")
    
    #Fisherman on Isle of Eigg
    # => Suppose he supplies the restaurants
    relationships["Stuart Millar"].extend(["Galmisdale Cafe", "Lagerona"])
    
    #Crofters on Isle of Eigg
    # => Suppose they supply the Eigg Shop (e.g. with Eggs & Vegetables)
    relationships["Lucy Conway"].append("Eigg Shop")
    relationships["Eddie Scott"].append("Eigg Shop")
    
    #Article says that Libby Galli easrns "Most of her income serving tea to toursits" and baking cake
    # => Presumably she is either a cafe employee or supplies the cafe with cake
    relationships["Libby Galli"].append("Galmisdale Cafe")
    
    #Crofter on Isle of Eigg
    # => Suppose they supply the Eigg Shop (e.g. with Eggs & Vegetables)
    relationships["Mairi McKinnon"].append("Eigg Shop")

    return relationships

def fetchRawCSVObservationData(filename):
    data = pd.read_csv(filename) 
    df = data[['Recorder', 'Latitude (WGS84)', 'Longitude (WGS84)', 'Start date year', 'End date year','Scientific name', 'Common name']]

    df = df.dropna(subset=['Latitude (WGS84)'])
    df = df.dropna(subset=['Longitude (WGS84)'])
    df["Latitude (WGS84)"] = df["Latitude (WGS84)"].astype(np.float32)
    df["Longitude (WGS84)"] = df["Longitude (WGS84)"].astype(np.float32)

    return df

#default pandas dataframe
def eiggRawData():
    df = fetchRawCSVObservationData(islandDatasets+"eigg.csv")
    
    df = df.dropna(subset=['Start date year'])
    df["Start date year"] = df["Start date year"].astype(np.int32)

    return df

def muckRawData():
    df = fetchRawCSVObservationData(islandDatasets+"muck.csv")
    
    df = df.dropna(subset=['Start date year'])
    df["Start date year"] = df["Start date year"].astype(np.int32)

    return df

def skyeRawData():
    df = fetchRawCSVObservationData(islandDatasets+"skye.csv")
    
    df = df.dropna(subset=['Start date year'])
    df["Start date year"] = df["Start date year"].astype(np.int32)

    return df

def rumRawData():
    df = fetchRawCSVObservationData(islandDatasets+"rum.csv")
    
    df = df.dropna(subset=['Start date year'])
    df["Start date year"] = df["Start date year"].astype(np.int32)

    return df

def validatedEiggData():
    with open(basedir+"crushedFoodWebDatasets/EiggVerifiedSpeciesList", "rb") as f:
        verifiedSpecies = pickle.load(f)

    df = fetchRawCSVObservationData(islandDatasets+"eigg.csv")
    df["Scientific name"] = df["Scientific name"].str.lower()
    df["Scientific name"] = df["Scientific name"].map(lambda x: mapRawNameToValidated(x,verifiedSpecies))

    # inferStartDateFromEndDate(df) => Decided not to use in production calling, for consistency purposes
    
    return df

def inferStartDateFromEndDate(df):
    try:
        if (not (row['End date year'].isnull())) and row['Start date year'].isnull():
            row['Start date year'] = row['End date year']
    except:
        pass

def mapRawNameToValidated(rawName,verifiedSpeciesDict):
    if rawName in verifiedSpeciesDict:
        return verifiedSpeciesDict[rawName]
    
    return rawName

def convertFrameCoordsToUsableLatLon(df):
    organised = list(zip(df['Latitude (WGS84)'],df['Longitude (WGS84)']))
    organised = list(map(lambda x: [float(x[0]),float(x[1])],organised))
    return organised
    
def prettyPrintDict(dict_):
    kz = dict_.keys()

    for k in kz:
        print(str(dict_[k]) + " " + "---" + " " + str(k))
