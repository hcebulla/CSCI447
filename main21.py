import random
import numpy
from numpy.core._multiarray_umath\
import ndarray
import pandas as pd


def ten_percenter(dataset):
    for i in range(int(numpy.ceil(len(dataset)/10))): #steps through the data set and rounds each value up to the nearest integer and takes 10%
        safe = dataset[i][:-1]
        random.shuffle(dataset)
        dataset[i][:-1] = safe #putting the data into a 'safe' array that doesnt have the first attribute
    return dataset

def CrossValSplit(dataset): #seperates the list into 10 sublists that then can be fed into the 10-fold cross validation
    random.shuffle(dataset) #shuffles the dataset before splitting
    for i in range(0,len(dataset),10):
        yield dataset[i:i+9]

def test_list(entry): #makes sure that the first attribute in the list is deleted before sending it out
    for i in entry:
        del i[0]

# this descritization function is used using the equal distance binning function with an interval of 15, note that the interval is random.
# the method was derived from : https://www.geeksforgeeks.org/ml-binning-or-discretization/
# Also, we are going to be smoothing by bin means

def descritization(dataset, numclass):
    interval : 15
    array = numpy.asarray(dataset)
    for i in range(dataset[0] -1): #excludes the class attribute
        array.sort() #sorts in ascending order as is needed
        array = numpy.split(array,15)
        for j in range(interval):
            tempavg = 0
            for z in array: #we first have to loop through the array to find the avg, then go back through and replace it with it
                tempavg += z[i]
            avg = tempavg/(len(array)) #finding the mean value
            for z in array:
                array[i] = avg + 1 # we are adding 1 as requested in the rubric
    return array

#this method was derived from https://stackoverflow.com/questions/43442072/pandas-how-can-i-do-cross-validation-without-using-scikit

def TFCross(train_set):
    k = 10
    folds = numpy.array_split(train_set,k)
    for i in range(10)
        train = folds.copy()
        del train[i]
        train = pd.concat(train, sort= False)
        work(clf, train.copy(), test.copy())

def work(clf, train.copy(), test.copy()):
    orig_dataset = copy.copy(dataset) # keeping a copy of the non tested dataset
    dataset = ten_percenter(dataset)
    orig_dataset = CrossValSplit(orig_dataset)
    clf.fit(train)
    return clf.score(test_list(dataset))

















