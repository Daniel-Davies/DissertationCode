def exchangesByBusiness():
    relationships = {}

    relationships["Eiggy Bread"] = ["Glebe Barn"]
    relationships["Massage Theraphy"] = ["Lagerona", "Glebe Barn", "Kildonnan House"] #suppose she services the main residences with a massage
    relationships["Sandavore Farm"] = ["Eigg Shop"]
    relationships["Stuart Millar Fishing"] = ["Eigg Shop", "Galmisdale Cafe"]
    relationships["Laig Bay Brewing"] = ["Galmisdale Cafe", "Lagerona"]
    relationships["Eddie's Eigg Croft"] = ["Eigg Crafts"]
    relationships["Kildonnan Bay Oysters"] = ["Eigg Shop", "Galmisdale Cafe"]
    relationships["Eigg Organics"] = ["Eigg Shop"]
    relationships["Libby Galli Felt"] = ["Eigg Crafts"]
    relationships["Kildonnan House"] = ["Lagerona"]
    relationships["Lost Map Records"] = ["Eigg Crafts"]
    relationships["Laig Farm"] = ["Eigg Shop", "Galmisdale Cafe"]
    relationships["Anead hand knitwear"] = ["Eigg Crafts"]
    relationships["Lagerona"] = ["Kildonnan House"]
    relationships["Hebnet Cic"] = ["Lagerona", "Kildonnan House", "Glebe Barn"]
    relationships["Scottish Willow Baskets"] = ["Eigg Crafts"]

    return relationships

import sys
sys.path.insert(0,'./..')
from anonymisationTools import *

def inferredExchangeNets():
    return accessAnonymisedDataDict('inferredExchangeNets')

def exportTags():
    return accessAnonymisedDataDict('exportTags')

def exportOnlyGraph():
    baseNet = inferredExchangeNets()
    xp = exportTags()

    for item in baseNet:
        if xp[item] == 0:
            baseNet[item] = []
    
    return baseNet

def nonExportOnlyGraph():
    baseNet = inferredExchangeNets()
    xp = exportTags()

    for item in baseNet:
        if xp[item] == 1:
            baseNet[item] = []
    
    return baseNet