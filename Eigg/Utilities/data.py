import pandas as pd
import numpy as np
import pickle
from anonymisationTools import anonymiseDataDict, accessAnonymisedDataDict
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
    return accessAnonymisedDataDict('uninferredNamesGraphRaw')

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
    relationships["Small Isles Medical Centre"] = []
    
    return relationships

def inferredNamesGraph():
    return accessAnonymisedDataDict('inferredNamesGraphRaw')

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

# if __name__=="__main__":
#     data = uninferredNamesGraph()
#     print(data)
    
def incorporationDates():
    relationships = {}

    # PRETTY SURE BUT NOT 100% SURE
    relationships["Galmisdale Cafe"] = 2010 #https://smallseotools.com/domain-age-checker/ => use www.galmisdale-bay.com
    relationships["Eddie's Eigg Croft"] = 2010 #https://www.bbc.co.uk/news/uk-scotland-highlands-islands-11668830, https://www.scotsman.com/news/eigg-and-spoon-man-fight-save-bluebells-1698075
    relationships["Sandavore Farm"] = 2010 #https://www.linkedin.com/in/alex-boden-5a65b855/?originalSubdomain=uk
    relationships["Eigg Yurts"] = 2012 #https://www.airbnb.co.uk/rooms/438562?source_impression_id=p3_1587838651_OBY%2BVPTwy5T87Xh2&guests=1&adults=1
    relationships["Craigard Teas"] = 2013 #https://www.facebook.com/CraigardTeas/?ref=page_internal
    relationships["Glebe Barn"] = 1999 # POST BUYOUT I THINK (??)http://www.spanglefish.com/eigghistorysociety/index.asp?pageid=666853
    relationships["Kildonnan House"] = 1996 #WAS RUN PRE-BUYOUT #http://www.spanglefish.com/eigghistorysociety/index.asp?pageid=666853

    # CONFIRMED
    relationships["Heritage Trust"] = 1996 #https://beta.companieshouse.gov.uk/company/SC170339
    relationships["Eigg Crafts"] = 1998 #https://beta.companieshouse.gov.uk/company/SC188634
    relationships["Clean Planet Now"] = 2016 #https://beta.companieshouse.gov.uk/company/SC544049
    relationships["Eigg Electric"] = 2005 #https://beta.companieshouse.gov.uk/company/SC293992
    relationships["Eigg Trading"] = 1997 #https://beta.companieshouse.gov.uk/company/SC177386
    relationships["Eigg Construction"] = 1999 #https://beta.companieshouse.gov.uk/company/SC202238
    relationships["Eigg Eco Centre"] = 2002 #http://www.earthconnections.co.uk/eco-courses/residential-eco-courses ## APPROXIMATION
    relationships["Eigg Huts"] = 2017 #https://beta.companieshouse.gov.uk/company/SC554221
    relationships["Hebnet Cic"] = 2011 #https://beta.companieshouse.gov.uk/company/SC399079
    relationships["Eiggy Bread"] = 2012 #https://www.facebook.com/pg/EiggyBread/about/?ref=page_internal
    relationships["Eigg Adventures"] = 2009 #https://twitter.com/eiggadventures
    relationships["Eigg Camping Pods"] = 2016 #http://www.eiggadventures.co.uk/camping-pods/
    relationships["Eigg History"] = 1999 #http://www.spanglefish.com/eigghistorysociety/
    relationships["Kildonnan Bay Oysters"] = 2018 #https://twitter.com/eiggoysters?lang=en
    relationships["Equilibrium Eigg Massage Therapy"] = 2007 #https://eiggmassagetherapy.wordpress.com/about/
    relationships["A Nead Knitwear"] = 2009 #https://anneadhandknitwear.co.uk/about/
    relationships["Laig Bay Brewing"] = 2014 #https://books.google.co.uk/books?id=Nk1yDwAAQBAJ&pg=PT2790&lpg=PT2790&dq=laig+bay+brewing+%222014%22&source=bl&ots=YA4nBAN5eQ&sig=ACfU3U0vkkz9-tI5CeSgKKkY8aVIhcqcQg&hl=en&sa=X&ved=2ahUKEwiRvIO3lITpAhX8QRUIHW-HAKMQ6AEwBHoECAoQAQ#v=onepage&q=laig%20bay%20brewing%20%222014%22&f=false
    relationships["Sweeney's Bothy"] = 2011 #http://www.thebothyproject.org/about/
    relationships["Eigg Shed"] = 2017 #https://www.visitscotland.com/info/accommodation/eigg-huts-amazing-eigg-shed-p1520831 => Part of Eigg Huts so by extension is 2017
    relationships["Eigg Shop"] = 1997 #https://isleofeiggshop.com/

    # TOTALLY GUESSED
    relationships["Lagerona"] = 2008 #suppose it opened as a guest house after the pier opened, due to attracted tourists
    relationships["The Bothy Cuagach"] = 1997      #https://homeandspirit.wordpress.com/tag/bothy/ => It's 19th century but i presume only available to stay in post-buyout
    relationships["Eigg Organics"] = 1996 # Neil worked as a handyman for schellenberg so let's say they opened before https://greenadventurestravel.com/Features/eigg.html
    relationships["Small Isles Medical Centre"] = 2016
    
    return relationships

def grantsByYear():
    # Does NOT include bank loans
    # Also just an unknown amount from online or cheque donations

    relationships = {}

    #https://www.tnlcommunityfund.org.uk/funding/grants/recipients/GB-SC-SC025609
    #https://www.tnlcommunityfund.org.uk/funding/grants/recipients/GB-SC-SC026876
    #http://isleofeigg.org/ieht/community-buyout/
    #http://gotlottery.uk/scotland/highland/isle-of-eigg

    ## GRANT JUNKIES XD XD XD 
    #https://www.theguardian.com/uk-news/2017/sep/26/this-island-is-not-for-sale-how-eigg-fought-back

    #2019
    #https://www.calmac.co.uk/2000-boost-for-Eigg-Gaelic-youth-project
    #https://www.highland.gov.uk/news/article/11862/council_welcomes_14m_funding_from_the_rural_tourism_infrastructure_fund_rtif

    #20000 in 2010 for power grid
    #https://www.bbc.co.uk/news/10449367

    #Most recent (2020+)
    #https://www.highland.gov.uk/news/article/12355/highland_welcomes_rcgf_funds_for_local_communities

    #https://www.tnlcommunityfund.org.uk/funding/grants?q=Eigg&westminsterConstituency=S14000039

    #the 23760 grant
    #https://www.creativescotland.com/what-we-do/latest-news/archive/2019/05/create-inclusion

    #EU funding
    #https://ec.europa.eu/regional_policy/en/projects/united-kingdom/eigg-goes-green

    # Big Green Challenge
    #http://news.bbc.co.uk/1/hi/scotland/highlands_and_islands/8457768.stm

    #https://www.pressreader.com/uk/scottish-daily-mail/20170516/281848643529519

    #Nursery Fund
    #http://www.gebfoundation.com/local-organisations-are-invited-to-consider-applying-for-funding-from-the-gordon-and-ena-baxter-foundation

    #Pier fund
    #https://www.heraldscotland.com/opinion/13089560.the-highland-line-why-five-island-communities-are-hacked-off-over-ferries/
    #https://www.theguardian.com/uk/2003/aug/04/kirstyscott

    relationships[2021] = [1100000]
    relationships[2020] = [100000]
    relationships[2019] = [2000,273632,23760] 
    relationships[2018] = [10000,3000]
    relationships[2017] = [4792,10000,34311,130000]
    relationships[2016] = [5771]
    relationships[2015] = [11803]
    relationships[2014] = [9100,6500,6784,17000,3550]
    relationships[2013] = [7000,8000,1768]
    relationships[2012] = []
    relationships[2011] = [5185,2000]
    relationships[2010] = [4150,20000,300000]
    relationships[2009] = [4300]
    relationships[2008] = [8434,3900,9290]
    relationships[2007] = [3500, 8671, 4995]
    relationships[2006] = []
    relationships[2005] = [250000,3850,2865,667770]
    relationships[2004] = [5000]
    relationships[2003] = [101378, 2000,7800000]
    relationships[2002] = [2820, 4867]
    relationships[2001] = []
    relationships[2000] = [4342]
    relationships[1999] = [91985]
    relationships[1998] = [3453]
    relationships[1997] = [1505,1500000,17000]
    relationships[1996] = []

    return relationships

if __name__=="__main__":
    x = grantsByYear()

    total = 0
    for item in x:
        total += sum(x[item])
    
    print(total)

def populationStats():
    relationships = {}

    relationships[2021] = 105
    relationships[2020] = 105
    relationships[2019] = 105 
    relationships[2018] = 105
    relationships[2017] = 105
    relationships[2016] = 83
    relationships[2015] = 83
    relationships[2014] = 83
    relationships[2013] = 83
    relationships[2012] = 83
    relationships[2011] = 83
    relationships[2010] = 87
    relationships[2009] = 87
    relationships[2008] = 87
    relationships[2007] = 87
    relationships[2006] = 87
    relationships[2005] = 87
    relationships[2004] = 67
    relationships[2003] = 67
    relationships[2002] = 67
    relationships[2001] = 67
    relationships[2000] = 64
    relationships[1999] = 64
    relationships[1998] = 64
    relationships[1997] = 64
    relationships[1996] = 64

    return relationships
