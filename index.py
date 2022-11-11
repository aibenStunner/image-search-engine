"""
USAGE 

python3 index.py --dataset dataset --index index.csv
"""

from scripts.colordescriptor import ColorDescriptor
import argparse 
import glob 
import cv2


# construct the arugment parser and parse the arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to hte directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True, help="path to where the computed index will be stored")
args = vars(ap.parse_args())

# initialize the color descriptor 
# 8 hue bins  12 Saturation bins  3 value bins
cd = ColorDescriptor((8, 12, 3))

# open the output index file for writing 
output = open(args["index"], "w")

# use glob to grab the image paths and loop over them 
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # extract the image ID(i.e. the unique filename) from the image path and load the image itself 
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    # describe the image 
    features = cd.describe(image)

    # write the features to file 
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file 
output.close()
