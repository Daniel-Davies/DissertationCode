
from faker import Factory
from collections import defaultdict
from data import *

if __name__=="__main__":
    fakeNameGen  = Factory.create()
    fakeNames  = defaultdict(fakeNameGen.name)
    data = inferredNamesGraph()
    for name in data:
        newName = fakeNames[name]
    
    with open('anonymisedNameMappings','wb') as f:
        pickle.dump(fakeNames,f)

    print("DONE!")

    with open('anonymisedNameMappings','rb') as f:
        new = pickle.load(f)
    
    print(new)
    