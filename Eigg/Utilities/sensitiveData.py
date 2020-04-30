def uninferredNamesGraphRaw():
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

def inferredNamesGraphRaw():
    relationships = uninferredNamesGraphRaw()
    
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

def coOwnerNetworkRaw():
    relationships = {}
    
    relationships["Damian Helliwell"] = ["Heritage Trust"]
    relationships["Margaret Fyffe"] = ["Clean Planet Now", "Heritage Trust", "Eigg Electric", "Eigg Trading", "Eigg Construction", "The Bothy Cuagach"]
    relationships["Norah Barnes"] = ["Clean Planet Now", "Heritage Trust", "Eigg Eco Centre"]
    relationships["Elizabeth Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Shed", "Sandavore Farm", "Eigg Trading"]
    relationships["Lucy Conway"] = ["Heritage Trust", "Sweeney's Bothy", "Eddie's Eigg Croft"] #accountant, wife to eddie
    relationships["Sarah Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Electric", "Sandavore Farm", "Kildonnan Bay Oysters"]
    relationships["Mark Alan Foxwell"] = ["Heritage Trust"]
    relationships["Jacqueline Kirk"] = ["Heritage Trust"] #Sue is the owner of the shop => https://vimeo.com/81932195
    relationships["Ian Leaver"] = ["Heritage Trust"]
    relationships["Stuart McCarthy"] = ["Glebe Barn","Heritage Trust", "Laig Bay Brewing", "Eigg Construction"] #supplies restaurants with beer 
    relationships["Tasha McVarish"] = ["Heritage Trust", "Equilibrium Eigg Massage Therapy"]
    
    relationships["Sue Hollands"] = ["Eigg Organics", "Eigg Electric"]
    relationships["Neil Robertson"] = ["Eigg Organics"]
    
    relationships["Sue Kirk"] = ["Lagerona", "Eigg Construction"] #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = ["Lagerona", "Eigg Construction"] ##INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = ["Taxi Service"]
    relationships["Libby Galli"] = []
    
    relationships["Eddie Scott"] = ["Sweeney's Bothy", "Eddie's Eigg Croft", "Eigg Electric"]
    
    relationships["Marie Carr"] = ["Kildonnan House"]
    relationships["Colin Carr"] = ["Kildonnan House", "Eigg Electric", "Eigg Construction"]
    relationships["Greg Carr"] = ["Kildonnan House", "Eigg Trading"]
    
    relationships["Alex Boden"] = ["Eigg Shed", "Sandavore Farm", "Eigg Huts", "Hebnet Cic"]
    
    relationships["Katrin Bach"] = ["Eiggy Bread"] #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = ["Glebe Barn", "Eigg Construction"]
    
    relationships["Simon Helliwell"] = ["Glebe Barn", "Hebnet Cic"] #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = ["Glebe Barn"] #daughter is now technically owner

    relationships["Louise Taylor"] = []
    relationships["Martin Merrick"] = []
    relationships["Kenneth Kean"] = []
    relationships["Amanda Moult"] = []
    relationships["Annabelle Scott-Moncrieff"] = []
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
    
    relationships["Jenny Robertson"] = ["A NEAD KNITWEAR"]
    
    relationships["Donna McCulloch"] = [] #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = ["Selkie Explorers"]
    
    ##basket making
    relationships["Catherine Davies"] = []
    relationships["Pascal Carr"] = []
    
    relationships["Stuart Fergusson"] = ["Eigg Trading", "Galmisdale Cafe"]
    
    relationships["Peter Wade-Martins"] = ["Tophouse"]
    relationships["Susanna Wade-Martins"] = ["Tophouse"]
    
    relationships["Jacky"] = ["TIGH AN SITHEAN"]
    relationships["Mick"] = ["TIGH AN SITHEAN"]
    
    relationships["Mairi McKinnon"] = []
    relationships["Clare Miller"] = ["Eigg Yurts"]
    
    relationships["John"] = ["Craigard Teas"]
    relationships["Sheila"] = ["Craigard Teas"] #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = ["Eigg History"]
    relationships["Hilda Ibrahim"] = []
    
    relationships["Ian Alexander James Bolas"] = ["Hebnet Cic"]
    relationships["David Byres Newton"] = ["Hebnet Cic"]
    relationships["Marc Allan Smith"] = ["Hebnet Cic"]
    
    relationships["Jennifer Leiper"] = ["Clean Planet Now"]
    relationships["Robert Wallace"] = ["Clean Planet Now"]
    relationships["Rosemary Jane Acock"] = ["Clean Planet Now"]
    
    return relationships
    
def salesTagsCoOwnersRaw():
    relationships = {}
    
    relationships["Damian Helliwell"] = 0
    relationships["Margaret Fyffe"] = 1
    relationships["Norah Barnes"] = 0
    relationships["Elizabeth Boden"] = 1
    relationships["Lucy Conway"] = 1
    relationships["Sarah Boden"] = 1
    relationships["Mark Alan Foxwell"] = 0
    relationships["Jacqueline Kirk"] = 0 #Sue is the owner of the shop => https://vimeo.com/81932195
    relationships["Ian Leaver"] = 0
    relationships["Stuart McCarthy"] = 1
    relationships["Tasha McVarish"] = 1
    
    relationships["Sue Hollands"] = 1
    relationships["Neil Robertson"] = 1
    
    relationships["Sue Kirk"] = 1 #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = 1  #INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = 1
    relationships["Libby Galli"] = 0
    
    relationships["Eddie Scott"] = 1
    
    relationships["Marie Carr"] = 1
    relationships["Colin Carr"] = 1
    relationships["Greg Carr"] = 1
    
    relationships["Alex Boden"] = 1
    
    relationships["Katrin Bach"] = 0 #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = 1
    
    relationships["Simon Helliwell"] = 1 #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = 1 #daughter is now technically owner

    relationships["Louise Taylor"] = 0
    relationships["Martin Merrick"] = 0
    relationships["Kenneth Kean"] = 0
    relationships["Amanda Moult"] = 0
    relationships["Annabelle Scott-Moncrieff"] = 0
    relationships["Laraine Wyn-Jones"] = 1
    relationships["Owain Wyn-Jones"] = 1
    
    #SAME GUY?!?!?!?!!?!?!
    relationships["John Christopher Lynch"] = 0
    relationships["John Christopher Clare"] = 0  
    relationships["John Booth"] = 0
    
    relationships["George Carr"] = 0 ##SHEEP FARMING
    relationships["Saira Renny"] =  0
    
    relationships["Bob Wallace"] = 0
    
    relationships["Stuart Millar"] = 0
    
    relationships["Jenny Robertson"] = 0
    
    relationships["Donna McCulloch"] = 0 #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = 1
    
    ##basket making
    relationships["Catherine Davies"] = 0
    relationships["Pascal Carr"] = 0
    
    relationships["Stuart Fergusson"] = 1
    
    relationships["Peter Wade-Martins"] = 1
    relationships["Susanna Wade-Martins"] = 1
    
    relationships["Jacky"] = 1
    relationships["Mick"] = 1
    
    relationships["Mairi McKinnon"] = 0
    relationships["Clare Miller"] = 1
    
    relationships["John"] = 1
    relationships["Sheila"] = 1 #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = 0
    relationships["Hilda Ibrahim"] = 0
    
    relationships["Ian Alexander James Bolas"] = 0
    relationships["David Byres Newton"] = 0
    relationships["Marc Allan Smith"] = 0
    
    relationships["Jennifer Leiper"] = 0
    relationships["Robert Wallace"] = 0
    relationships["Rosemary Jane Acock"] = 0
    
    return relationships

def locationsPerPerson():
    residences = {}

    residences['Mairi McKinnon'] = [('56.9018832,-6.1449375', "Maranatha (7 Cleadale)")] # https://sjsa.wordpress.com/tag/eigg/s
    residences['Neil Robertson'] = [('56.922044,-6.1446842', "Eigg Organics")]
    residences['Kenneth Kean'] = [('56.8778059,-6.1337137','Pier Cottage')] # https://beta.companieshouse.gov.uk/company/SC554221/officers, http://isleofeigg.org/accommodation/the-smiddy/
    residences['Bob Wallace'] = [('56.8804647,-6.1417635', "Earth Connections Eco Centre")] # PROBABLY NOT REAL ADDRESS => https://beta.companieshouse.gov.uk/officers/x-151T1pEie2etTsFQ-zjg9LejI/appointments
    residences['George Carr'] = [('56.9131675,-6.1619473', "Laig Farm")]
    residences['John Booth'] = [('56.878903, -6.146895', "Galmisdale House")] #https://beta.companieshouse.gov.uk/company/SC170339/officers => I presume it means Galmisdale House
    residences['Alex Boden'] = [('56.8849159,-6.1415287', "Sandavore Farm")]
    residences['Eddie Scott'] = [('56.9222615,-6.1420233', "Eddie's Eigg Croft")]
    residences['Pascal Carr'] = [('56.918268, -6.154348', "Shore Cottage")]
    residences['Stuart Millar'] = [('56.9269519,-6.1439637', "Howlin House")]
    residences['Colin Carr'] = [('56.8889489,-6.1250917', "Kildonnan house")]
    residences['Marie Carr'] = [('56.8889489,-6.1250917', "Kildonnan house")]
    residences['Simon Helliwell'] = [('56.8902145,-6.1343823', "Glebe Barn")] #ok technically they USED to live here, but thats fine since thats when a lot of observations will overlap anyway
    residences['Karen Helliwell'] = [('56.8902145,-6.1343823', "Glebe Barn")]
    residences['Katrin Bach'] = [('56.9113759,-6.1654777', "Laig")] # https://en-gb.facebook.com/EiggyBread/

    # residences['stuart fergusson'] #couldn't get address
    # residences['jenny robertson'] #couldn't get address

    return residences

def ownershipGraph():
    relationships = {}
    
    relationships["Damian Helliwell"] = ["Heritage Trust"]
    relationships["Margaret Fyffe"] = ["Heritage Trust", "Eigg Electric", "Eigg Trading", "Eigg Construction", "The Bothy Cuagach"]

    relationships["Norah Barnes"] = ["Heritage Trust"]
    relationships["Elizabeth Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Shed", "Sandavore Farm", "Eigg Trading"]
    relationships["Lucy Conway"] = ["Heritage Trust", "Sweeney's Bothy", "Eddie's Eigg Croft"] #accountant, wife to eddie
    relationships["Sarah Boden"] = ["Eigg Huts", "Heritage Trust", "Eigg Electric", "Sandavore Farm", "Kildonnan Bay Oysters"]
    relationships["Mark Alan Foxwell"] = ["Heritage Trust"]
    relationships["Jacqueline Kirk"] = ["Heritage Trust"]
    relationships["Ian Leaver"] = ["Heritage Trust"]
    relationships["Stuart McCarthy"] = ["Glebe Barn","Heritage Trust", "Laig Bay Brewing", "Eigg Construction"] #supplies restaurants with beer 
    relationships["Tasha McVarish"] = ["Heritage Trust", "Equilibrium Eigg Massage Therapy"]
    
    relationships["Sue Hollands"] = ["Eigg Organics", "Eigg Electric"]
    relationships["Neil Robertson"] = ["Eigg Organics"]
    
    relationships["Sue Kirk"] = ["Lagerona", "Eigg Construction"] #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = ["Lagerona", "Eigg Construction"] ##INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = []
    relationships["Libby Galli"] = []
    
    relationships["Eddie Scott"] = ["Sweeney's Bothy", "Eddie's Eigg Croft", "Eigg Electric"]
    
    relationships["Marie Carr"] = ["Kildonnan House"]
    relationships["Colin Carr"] = ["Kildonnan House", "Eigg Electric", "Eigg Construction"]
    relationships["Greg Carr"] = ["Kildonnan House", "Eigg Trading"]
    
    relationships["Alex Boden"] = ["Eigg Shed", "Sandavore Farm", "Eigg Huts", "Hebnet Cic"]
    
    relationships["Katrin Bach"] = ["Eiggy Bread"] #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = ["Glebe Barn", "Eigg Construction"]
    
    relationships["Simon Helliwell"] = ["Hebnet Cic"] #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = [] #daughter is now technically owner

    relationships["Louise Taylor"] = []
    relationships["Martin Merrick"] = []
    relationships["Kenneth Kean"] = []
    relationships["Amanda Moult"] = []
    relationships["Annabelle Scott-Moncrieff"] = []
    relationships["Laraine Wyn-Jones"] = ["Eigg Adventures", "Eigg Camping Pods", "Eigg Trading"]
    relationships["Owain Wyn-Jones"] = ["Eigg Adventures", "Eigg Camping Pods"]
    
    relationships["John Christopher Lynch"] = ["LOST MAPS RECORDS LTD"]
    relationships["John Christopher Clare"] = ["Eigg Electric"]
    relationships["John Booth"] = ["Eigg Electric", "Eigg Construction"]
    
    relationships["George Carr"] = ["Laig Farm"] ##SHEEP FARMING
    relationships["Saira Renny"] = ["Laig Farm"]
    
    relationships["Bob Wallace"] = []
    
    relationships["Stuart Millar"] = []
    
    relationships["Jenny Robertson"] = ["A NEAD KNITWEAR"]
    
    relationships["Donna McCulloch"] = [] #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = ["Selkie Explorers"]
    
    ##basket making
    relationships["Catherine Davies"] = []
    relationships["Pascal Carr"] = []
    
    relationships["Stuart Fergusson"] = ["Eigg Trading", "Galmisdale Cafe"]
    
    relationships["Peter Wade-Martins"] = ["Tophouse"]
    relationships["Susanna Wade-Martins"] = ["Tophouse"]
    
    relationships["Jacky"] = ["TIGH AN SITHEAN"]
    relationships["Mick"] = ["TIGH AN SITHEAN"]
    
    relationships["Mairi McKinnon"] = []
    relationships["Clare Miller"] = ["Eigg Yurts"]
    
    relationships["John"] = ["Craigard Teas"]
    relationships["Sheila"] = ["Craigard Teas"] #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = ["Eigg History"]
    relationships["Hilda Ibrahim"] = []
    
    relationships["Ian Alexander James Bolas"] = ["Hebnet Cic"]
    relationships["David Byres Newton"] = ["Hebnet Cic"]
    relationships["Marc Allan Smith"] = ["Hebnet Cic"]
    
    relationships["Jennifer Leiper"] = []
    relationships["Robert Wallace"] = []
    relationships["Rosemary Jane Acock"] = []
    
    return relationships

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

def inferredExchangeNets():
    relationships = {}

    relationships["Elizabeth Boden"] = ["Eigg Shop"]
    relationships["Lucy Conway"] = ["Eigg Crafts"] #eddie's eigg crofts supplies with bluebell seeds; https://www.bbc.co.uk/news/uk-scotland-highlands-islands-11668830
    relationships["Sarah Boden"] = ["Eigg Shop", "Galmisdale Cafe"] #Suppose the oysters are sold at the cafe for lunch 
    relationships["Tasha McVarish"] = ["Lagerona", "Glebe Barn", "Kildonnan House"] #suppose she services the main residences with a massage
    relationships["Sue Hollands"] = ["Eigg Shop"] #from Eigg Organics
    relationships["Neil Robertson"] = ["Eigg Organics"] #from Eigg Organics
    relationships["Libby Galli"] = ["Eigg Crafts"]
    relationships["Eddie Scott"] = ["Eigg Crafts"]
    relationships["Marie Carr"] = ["Lagerona"] # they probably send their extra traffic the other way too
    relationships["Colin Carr"] = ["Lagerona"]
    relationships["Greg Carr"] = ["Lagerona"]
    relationships["Alex Boden"] = ["Eigg Shop"]
    relationships["Katrin Bach"] = ["Glebe Barn"] #caterer for Glebe barn
    relationships["John Christopher Lynch"] = ["Eigg Crafts"] # suppose he sells his music in eigg craft
    relationships["George Carr"] = ["Eigg Shop", "Galmisdale Cafe"] ##SHEEP FARMING
    relationships["Saira Renny"] = ["Eigg Shop", "Galmisdale Cafe"]
    relationships["Stuart Millar"] = ["Galmisdale Cafe"]
    relationships["Jenny Robertson"] = ["Eigg Crafts"] # from the ANEAD crafts
    relationships["Donna McCulloch"] = ["Eigg Crafts"] #Technically "Creative Eigg"
    ##basket making
    relationships["Catherine Davies"] = ["Eigg Crafts"]
    relationships["Pascal Carr"] = ["Eigg Crafts"]
    relationships["Camille Dressler"] = ["Eigg Crafts"]
    relationships["Hilda Ibrahim"] = ["Eigg Crafts"]
    
    relationships["Damian Helliwell"] = ["Eigg Crafts"]
    relationships["Margaret Fyffe"] = []
    relationships["Norah Barnes"] = []
    relationships["Mark Alan Foxwell"] = []
    relationships["Jacqueline Kirk"] = []
    relationships["Ian Leaver"] = []
    relationships["Stuart McCarthy"] = ["Galmisdale Cafe", "Lagerona"] 
    relationships["Sue Kirk"] = ["Kildonnan House"] #send overlf
    relationships["Alisdair Kirk"] = [] 
    relationships["Charlie Galli"] = []        
    
    relationships["Tamsin McCarthy"] = []
    
    relationships["Simon Helliwell"] = ["Glebe Barn"] 
    relationships["Karen Helliwell"] = ["Glebe Barn"] 

    relationships["Louise Taylor"] = []
    relationships["Martin Merrick"] = []
    relationships["Kenneth Kean"] = []
    relationships["Amanda Moult"] = []
    relationships["Annabelle Scott-Moncrieff"] = []
    relationships["Laraine Wyn-Jones"] = []
    relationships["Owain Wyn-Jones"] = []
    
    relationships["John Christopher Clare"] = []
    relationships["John Booth"] = []
    relationships["Bob Wallace"] = []    
    relationships["Celia Bull"] = []
    relationships["Stuart Fergusson"] = []
    
    relationships["Peter Wade-Martins"] = []
    relationships["Susanna Wade-Martins"] = []
    
    relationships["Jacky"] = []
    relationships["Mick"] = []
    
    relationships["Mairi McKinnon"] = []
    relationships["Clare Miller"] = []
    
    relationships["John"] = []
    relationships["Sheila"] = [] #John Clare and Sheila Gunn 
    relationships["Ian Alexander James Bolas"] = []
    relationships["David Byres Newton"] = []
    relationships["Marc Allan Smith"] = []
    
    relationships["Jennifer Leiper"] = []
    relationships["Robert Wallace"] = []
    relationships["Rosemary Jane Acock"] = []
    
    return relationships

def exportTags():

    #Clean Planet Now =>  "organise residential courses on sustainable living." => http://www.cleanplanetnow.com/index.php/about/who-we-are
    relationships = {}
    
    relationships["Damian Helliwell"] = 1 # 'Exports' music/appearances => https://www.ticketsource.co.uk/whats-on/glenuig/glenuig-hall/album-launch-of-damian-helliwells-metta/e-gdyme
    relationships["Margaret Fyffe"] = 0
    relationships["Norah Barnes"] = 0
    relationships["Elizabeth Boden"] = 0
    relationships["Lucy Conway"] = 1 #work for export since Eddie's Eigg Croft export bluebells eddieseiggcroft.com/index.asp?pageid=228322

    #posted YESTERDAY (10/03) about planned expansion for oysters
    #https://twitter.com/EiggOysters?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor
    relationships["Sarah Boden"] = 0
    relationships["Mark Alan Foxwell"] = 0
    relationships["Jacqueline Kirk"] = 0
    relationships["Ian Leaver"] = 0
    relationships["Stuart McCarthy"] = 1 # exports beer => https://laigbaybrewingco.wordpress.com/buy-our-beer/
    relationships["Tasha McVarish"] = 0
    
    relationships["Sue Hollands"] = 0
    relationships["Neil Robertson"] = 0
    
    relationships["Sue Kirk"] = 0 # Marking 1 for significant imports (runs shop)
    relationships["Alisdair Kirk"] = 0
    
    relationships["Charlie Galli"] = 0
    relationships["Libby Galli"] = 1 #exports/ sells felt art http://libbygallifeltartist.co.uk/about.html
    
    relationships["Eddie Scott"] = 1 #work for export since Eddie's Eigg Croft export bluebells eddieseiggcroft.com/index.asp?pageid=228322, https://www.bbc.co.uk/news/uk-scotland-highlands-islands-11668830
    
    relationships["Marie Carr"] = 0
    relationships["Colin Carr"] = 0
    relationships["Greg Carr"] = 0
    
    relationships["Alex Boden"] = 0
    
    relationships["Katrin Bach"] = 0
    
    relationships["Tamsin McCarthy"] = 1 # presumed to be involved with export of beer with stuart
    
    relationships["Simon Helliwell"] = 0
    relationships["Karen Helliwell"] = 0

    relationships["Louise Taylor"] = 0
    relationships["Martin Merrick"] = 0
    relationships["Kenneth Kean"] = 0
    relationships["Amanda Moult"] = 0
    relationships["Annabelle Scott-Moncrieff"] = 0
    relationships["Laraine Wyn-Jones"] = 0
    relationships["Owain Wyn-Jones"] = 0
    
    relationships["John Christopher Lynch"] = 1 #https://www.heraldscotland.com/arts_ents/14721189.island-life-pictish-trails-johnny-lynch-on-eigg-friendship-his-new-album-and-leaving-fence-records/
    relationships["John Christopher Clare"] = 0
    relationships["John Booth"] = 0
    
    relationships["George Carr"] = 0 ##SHEEP FARMING => https://www.telegraph.co.uk/news/uknews/1396984/Independence-was-best-thing-weve-done-say-islanders.html
    relationships["Saira Renny"] = 0
    
    relationships["Bob Wallace"] = 0
    
    relationships["Stuart Millar"] = 0
    
    relationships["Jenny Robertson"] = 1 #knitwear => https://anneadhandknitwear.co.uk/product/white-long-cobweb-fingerless-gloves/
    
    relationships["Donna McCulloch"] = 0
    
    relationships["Celia Bull"] = 0
    
    ##basket making
    relationships["Catherine Davies"] = 1 # https://all-about-willow.co.uk/content/aboutus/2173/ + https://themakers.directory/craft-directory-members/catherinefdaviesgmail-com/products/
    relationships["Pascal Carr"] = 1
    
    relationships["Stuart Fergusson"] = 0
    
    relationships["Peter Wade-Martins"] = 0
    relationships["Susanna Wade-Martins"] = 0
    
    relationships["Jacky"] = 0
    relationships["Mick"] = 0    
    relationships["Mairi McKinnon"] = 0
    relationships["Clare Miller"] = 0
    
    relationships["John"] = 0
    relationships["Sheila"] = 0 #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = 1
    relationships["Hilda Ibrahim"] = 0
    
    #hebnet cic, heaquartered on Eigg, operates in all of west scotland not just Eigg => https://www.ispreview.co.uk/index.php/2018/03/salmon-farmer-helps-bring-wireless-broadband-to-west-scotland.html
    relationships["Ian Alexander James Bolas"] = 1
    relationships["David Byres Newton"] = 1
    relationships["Marc Allan Smith"] = 1
    
    relationships["Jennifer Leiper"] = 0
    relationships["Robert Wallace"] = 0
    relationships["Rosemary Jane Acock"] = 0
    
    return relationships

#############################################################################################################################################################
#############################################################################################################################################################
# NON SENSITIVE DATA #
#############################################################################################################################################################
#############################################################################################################################################################

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

    return list(set(relationships.keys()))

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
    relationships["Small Isles Medical Centre"] = 2016 #https://www.scottish-islands-federation.co.uk/new-innovative-health-care-model-for-the-small-isles/
    
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