"""
USAGE 

python3 search.py --index index.csv --query queries/108100.png --result-path dataset
"""

from scripts.colordescriptor import ColorDescriptor
from scripts.searcher import Searcher
import argparse 
import cv2 


# construct the argument parser and parse the arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True, help="path to where the computed index has been stored")
ap.add_argument("-q", "--query", required=True, help="path to the query image")
ap.add_argument("-r", "--result-path", required=True, help="path to the result")
args = vars(ap.parse_args())

# initialize the image descriptor 
cd = ColorDescriptor((8, 12, 3))


# load the query image and describe it 
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search 
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query 
cv2.imshow("Query", query)

# loop over the results 
for (score, resultID) in results:
    # load the result image and display it 
    result = cv2.imread(args["result_path"] + "/" + resultID)
    cv2.imshow("Result", result)
    cv2.waitKey(0)

