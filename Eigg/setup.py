
import argparse
import sys
sys.path.insert(1,'./Utilities')
from anonymisationTools import anonymiseSensitiveData, dontAnonymiseData

parser = argparse.ArgumentParser(description='Arg Parser for anonymisation')
parser.add_argument('-NO-ANON', action="store_true", default=False)

if __name__=="__main__":
    cl = parser.parse_args()
    if cl.NO_ANON:
        dontAnonymiseData()
    else:
        anonymiseSensitiveData()

    
