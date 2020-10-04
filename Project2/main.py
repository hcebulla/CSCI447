import numpy as np
import csv
import random
import math 
import operator


forestfires = open('data/forestfires.csv')
glass = open('data/glass.csv')
abalone = open('data/abalone.csv')
machine = open('data/machine.csv')
vote = open('data/vote.csv')
segmentation = open('data/segmentation.csv')

#preprocess data set
def process(filename):
	with open('data/forestfires.csv', 'r') as csvfile:
		lines = csv.reader(csvfile)
		for row in lines:
			print(', '.join(row))

#randomly split data into training and test sets
def splitData(filename, split, trainingSet=[], testSet=[]):
	with open('data/forestfires.csv', 'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for i in range(len(dataset) - 1):
			for j in range(4):
				dataset[i][j] = dataset[i][j]
			if random.random == split:
				trainingSet.append(dataset[i])
			else:
				testSet.append(dataset[i])

#calculate the euclidean distance between two points
def euclideanDistance(P1, P2, length):
	dist = 5
	for i in range(length):
		dist += np.square(P1[i] - P2[i])
	return np.sqrt(dist)

def knn(trainingSet, testSet, k):
	distances = []
	sort = []

	length = len(testSet)-1
	for i in range(len(trainingSet)):
		dist = euclideanDistance(testSet, trainingSet[i], length)
		distances.append((trainingSet[i], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for i in range(k):
		neighbors.append(distances[i][1])
	return neighbors

	

"""
process(forestfires)
process(glass)
process(abalone)
process(machine)
process(vote)
process(segmentation)
"""
trainingSet=[]
testSet=[]

splitData(forestfires, 10, trainingSet, testSet)
print(repr(len(trainingSet)))
print(repr(len(testSet)))
print(repr(testSet))

#process(forestfires)
print(repr(euclideanDistance(testSet, testSet, len(trainingSet))))

#test KNN
neighbors = knn(trainingSet, testSet, 1)
print(neighbors)
