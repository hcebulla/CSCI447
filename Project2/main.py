import numpy
import csv
import random

forestfires = open('/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/forestfires.csv')
glass = open('/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/glass.csv')
abalone = open('/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/abalone.csv')
machine = open('/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/machine.csv')
vote = open('/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/vote.csv')
segmentation = open('/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/segmentation.csv')

#preprocess data set
def process(filename):
	with open('/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/forestfires.csv', 'r') as csvfile:
		lines = csv.reader(csvfile)
		for row in lines:
			print(', '.join(row))

#randomly split data into training and test sets
def splitData(filename, split, trainingSet=[], testSet=[]):
	with open('/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/forestfires.csv', 'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for i in range(len(dataset) - 1):
			#for j in range(4):
				#dataset[i][j] = dataset[i][j]
			if random.random < split:
				trainingSet.append(dataset[i])
			else:
				testSet.append(dataset[i])

process(forestfires)
process(glass)
process(abalone)
process(machine)
process(vote)
process(segmentation)

trainingSet=[]
testSet=[]

splitData(forestfires, 10, trainingSet, testSet)
print(repr(len(trainingSet)))
print(repr(len(testSet)))

