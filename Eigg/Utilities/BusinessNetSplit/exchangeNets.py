
def uninferredExchangeNets():
    relationships = {}
    
    relationships["Damian Helliwell"] = ["Eigg Crafts"]
    relationships["Margaret Fyffe"] = []
    relationships["Norah Barnes"] = []
    relationships["Elizabeth Boden"] = []
    relationships["Lucy Conway"] = [] #accountant, wife to eddie
    relationships["Sarah Boden"] = []
    relationships["Mark Alan Foxwell"] = []
    relationships["Jacqueline Kirk"] = []
    relationships["Ian Leaver"] = []
    relationships["Stuart McCarthy"] = ["Galmisdale Cafe", "Lagerona"] #supplies restaurants with beer 
    relationships["Tasha McVarish"] = []
    
    relationships["Sue Hollands"] = []
    relationships["Neil Robertson"] = []
    
    relationships["Sue Kirk"] = ["Kildonnan House"] #Kildonnan as they send extra traffic there as is Sister
    relationships["Alisdair Kirk"] = [] ##INFERRED Roadworkds => Contruction co 
    
    relationships["Charlie Galli"] = []
    relationships["Libby Galli"] = ["Eigg Crafts"]
    
    relationships["Eddie Scott"] = []
    
    relationships["Marie Carr"] = []
    relationships["Colin Carr"] = []
    relationships["Greg Carr"] = []
    
    relationships["Alex Boden"] = []
    
    relationships["Katrin Bach"] = ["Glebe Barn"] #caterer for Glebe barn
    
    relationships["Tamsin McCarthy"] = []
    
    relationships["Simon Helliwell"] = ["Glebe Barn"] #previous owner of glebe, along with karen hellwell
    relationships["Karen Helliwell"] = ["Glebe Barn"] #daughter is now technically owner

    relationships["Louise Taylor"] = []
    relationships["Martin Merrick"] = []
    relationships["Kenneth Kean"] = []
    relationships["Amanda Moult"] = []
    relationships["Annabelle Scott-Moncrieff"] = []
    relationships["Laraine Wyn-Jones"] = []
    relationships["Owain Wyn-Jones"] = []
    
    relationships["John Christopher Lynch"] = []
    relationships["John Christopher Clare"] = []
    relationships["John Booth"] = []
    
    relationships["George Carr"] = [] ##SHEEP FARMING
    relationships["Saira Renny"] = []
    
    relationships["Bob Wallace"] = []
    
    relationships["Stuart Millar"] = []
    
    relationships["Jenny Robertson"] = ["Eigg Crafts"]
    
    relationships["Donna McCulloch"] = ["Eigg Crafts"] #Technically "Creative Eigg"
    
    relationships["Celia Bull"] = []
    
    ##basket making
    relationships["Catherine Davies"] = ["Eigg Crafts"]
    relationships["Pascal Carr"] = ["Eigg Crafts"]
    
    relationships["Stuart Fergusson"] = []
    
    relationships["Peter Wade-Martins"] = []
    relationships["Susanna Wade-Martins"] = []
    
    relationships["Jacky"] = []
    relationships["Mick"] = []
    
    relationships["Mairi McKinnon"] = []
    relationships["Clare Miller"] = []
    
    relationships["John"] = []
    relationships["Sheila"] = [] #John Clare and Sheila Gunn 

    relationships["Camille Dressler"] = ["Eigg Crafts"]
    relationships["Hilda Ibrahim"] = ["Eigg Crafts"]
    
    relationships["Ian Alexander James Bolas"] = []
    relationships["David Byres Newton"] = []
    relationships["Marc Allan Smith"] = []
    
    relationships["Jennifer Leiper"] = []
    relationships["Robert Wallace"] = []
    relationships["Rosemary Jane Acock"] = []
    
    return relationships

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