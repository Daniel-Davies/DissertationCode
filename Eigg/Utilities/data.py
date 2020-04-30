import pandas as pd
import numpy as np
import pickle
from anonymisationTools import anonymiseDataDict, accessAnonymisedDataDict
# CONTAINS DICTIONARIES OF DOUBLE CHECKED LAT/LON POINTS PER OBS
import sensitiveData

basedir = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/Utilities/"
islandDatasets = "C:/Users/davie/Desktop/Masters/Dissertation/Code/DissertationCode/Eigg/IslandDatasets/"

def listedEiggHotels():
    return sensitiveData.listedEiggHotels()

def inferredBusinessLocations():
    return sensitiveData.inferredBusinessLocations()

def electricGrid():
    return sensitiveData.electricGrid()

## Residences locations
def pointsOfInterest():
    return sensitiveData.pointsOfInterest()

def residentialEntry():
    return sensitiveData.residentialEntry()

def uninferredNamesGraph():
    return accessAnonymisedDataDict('uninferredNamesGraphRaw')

def allBusinessNames():
    return sensitiveData.allBusinessNames()

def customByBusiness():
    return sensitiveData.customByBusiness()

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

def incorporationDates():
    return sensitiveData.incorporationDates()

def grantsByYear():
    return sensitiveData.grantsByYear()

def populationStats():
    return sensitiveData.populationStats()
