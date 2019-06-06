import math
import sys


class RocchioClassifier:

    def __init__(self, train_set):
        self.training_set = train_set
        self.class_centroids = {}
        self.training()

    def training(self):
        class_size = {}
        for doc in self.training_set:
            doc_class = self.training_set[doc][-1]
            if doc_class not in self.class_centroids.keys():
                self.class_centroids[doc_class] = self.training_set[doc][0:-1]
                class_size[doc_class] = 1
            else:
                self.class_centroids[doc_class] = [self.class_centroids[doc_class][i] + self.training_set[doc][0:-1][i]
                                                   for i in range(len(self.training_set[doc]) - 1)]
                class_size[doc_class] += 1
        for c in self.class_centroids.keys():
            for i in range(len(self.class_centroids[c])):
                self.class_centroids[c][i] /= float(class_size[c])

    def predict(self, document):
        """
        Predicts class of document
        Computes distance of doc from each centroid and returns the argmin
        :param document: list of binary values
        :return: predicted class
        """
        distances = {}
        for centroid in self.class_centroids:
            distances[centroid] = (self.eucildean_dist(self.class_centroids.get(centroid), document))
        return min(distances, key=distances.get)

    def eucildean_dist(self, list1, list2):
        """
        Calculates euclidean distance between two lists of doubles

        Assumes lists are of same length
        :param list1: list of doubles
        :param list2: list of doubles
        :return: distance, double
        """

        result = 0
        for i in range(len(list1)):
            result += (list1[i] - list2[i])**2
        return math.sqrt(result)
