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
