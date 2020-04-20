import numpy as np 
import csv 


class Searcher:
    def __init__(self, indexPath):
        # store our index path
        self.indexPath = indexPath 

    def search(self, queryFeatures, limit=10):
        # initialize the dictionary of results 
        results = {}
    
        # open the index file for reading 
        with open(self.indexPath) as f:
            # initialize the CSV reader 
            reader = csv.reader(f)

            # loop over the rows in the index 
            for row in reader:
                # parse out the image ID and features, then compute the chi-squared distance between the features in the index and the query features 
                features = [float(x) for x in row[1:]]
                d = self.chi2_distance(features, queryFeatures)

                # now that there's the distance between the tow feature vectors, the results dictionary can be updated -- the key is the current image ID
                # in the index and the value is the distance computed, representing how 'similar' the image in the index is to the query 
                results[row[0]] = d
                
                # images that have a chi-squared similarity of 0 will be deemed to be identical to each other. As the chi-squared similarity value increases, the images
                # are considered to be less similar to each other

            # close the reader 
            f.close()

        # sort the results, so that the smaller distances(i.e. the more relevant images are at the front of the list)
        results = sorted([(v, k) for (k, v) in results.items()])

        # return the (limited)results 
        return results[:limit]
    
    def chi2_distance(self, histA, histB, eps = 1e-10):
        # compute the chi-squared distance
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])

        # the optional eps value is used to prevent division-by-zero errors 
        # the function is used to compare discrete probability distributions 

        # return the chi-squared distance 
        return d
