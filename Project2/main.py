import numpy
import csv
import random

#preprocess data set
def process(filename):
	with open(r'/Users/hannahcebulla/Desktop/CSCI447/CSCI447/Project2/forestfires.csv') as csvfile:
		lines = csv.reader(csvfile)
		for row in lines:
			print(', '.join(row))

#split data into training and test sets
def splitData(filename, split, trainingSet=[], testSet=[])
	with open(

