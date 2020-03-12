import requests
import re

def standardiseNames(name):
    name = name.replace('"', '')
    name = name.replace("'",'')
    name = name.replace("?",'')
    name = name.split("/")
    name = name[0]
    name = re.sub(r'\([^)]*\)', '', name)
    name = name.strip()
    name = name.lower()
    return name

def cleanSpeciesName(name, verify=True):
    name = cleanEcologicalName(name)
    if verify:
        name = validateSingleName(name)
    return name

def cleanEcologicalName(name):
    name = re.sub(r'\{.*\}', '', name)
    name = re.sub(r'\(.*\)', '', name)
    name = name.split(" ")

    if "cf" in name:
        name.remove("cf")
    
    if "cf." in name:
        name.remove("cf.")

    if "sp." in name:
        name.remove("sp.")

    if "spp." in name:
        name.remove("spp.")
    
    if "sp" in name:
        name.remove("sp")

    if "spp" in name:
        name.remove("spp")
    
    if "agg" in name:
        name.remove("agg")
    
    if "agg." in name:
        name.remove("agg.")

    if "indet" in name:
        name.remove("indet")
    
    if "indet." in name:
        name.remove("indet.")

    name = name[:2]
    name = " ".join(name)

    name = name.split("/")
    name = name[0]

    name = name.replace('"', '')
    name = name.replace("'",'')
    name = name.replace("?",'')

    return name.strip().lower()

def validateSingleName(name,limit=100):
    callToValidateName = requests.get('http://resolver.globalnames.org/name_resolvers.json?names='+name)
    jsonRes = callToValidateName.json()['data'][0]
    try:
        if not jsonRes['is_known_name']:
            return jsonRes['results']['canonical_form']
        else:
            return " ".join(name.split(" ")[:limit])
    except:
        print("Error occured at "+str(name))
        return name