# This file runs our ten-fold cross validation of Naive Bayes
# Jordan Kelly, Hannah Cebulla, and Ryan Pallman

import numpy
import random
import setup_data
import copy
import naive_bayes as nb
import statistical_analysis as sa

# Number of classes variable.
classes = 0


# Get the data from our data file.
def get_list(input, character):
    base_data = setup_data.load_data(input, character)
    return base_data


# Splits the data into ten chunks for use in the cross validation function and scrambles the data before splitting.
def splitter(samples):
    samples = numpy.asarray(samples)  # converts list to numpy array
    random.shuffle(samples)  # scrambles rows
    samples = numpy.array_split(samples, 10)  # splits into 10 smaller lists
    return samples


# Scramble the data and run the cross validation on the scrambled data.
def scrambled_cv(dataset):
    random.shuffle(dataset)  # Mix the data up.
    cross_validate(dataset)


# Removes class attribute from the dataset that we're going to use for validation.
def make_test_set(input):
    if type(input) == numpy.ndarray:
        input = numpy.ndarray.tolist(input)
    for i in input:
        del i[-1]
    return input


# We used https://www.geeksforgeeks.org/ml-binning-or-discretization/ to help us get our binning working as intended.
def discretize_data(dataset):
    interval = 10
    new_array = numpy.asarray(dataset)
    for i in range(len(new_array[0]) - 1):
        new_array = sorted(new_array, key = lambda l: l[i])
        new_array = numpy.array_split(new_array, interval)
        for j in range(interval):
            temp = 0
            for row in new_array[j]:
                temp += row[i]
            average = temp / len(new_array[j])
            for row in new_array[j]:
                row[i] = average + 1
        new_array = flatten_list(new_array)  # returns array to 2d form before starting next iteration
    return new_array


# Flattens the list so our algorithm can be used.
def flatten_list(three_dim_list):
    flattened = []
    for two_dim_list in three_dim_list:  # the list being iterated through here is the one being removed
        for our_list in two_dim_list:  # this list is appended to the 'flattened' list, thus removing a layer of lists
            flattened.append(our_list)
    return flattened


# Our cross validation
def cross_validate(dataset):
    global classes
    backup_data = copy.copy(dataset)
    test_results = []
    stats = []
    backup_data = splitter(backup_data)
    for i in range(10):  # iterate over all ten subsets
        nb.freqTable = []
        to_learn = copy.copy(backup_data)  # Use an unaltered version of the dataset each time
        to_test = make_test_set(to_learn.pop(i))
        to_learn = flatten_list(to_learn)
        nb.train(to_learn)
        to_test = nb.classify(to_test)
        test_results.append(to_test)
        stats.append(analyze(backup_data[i], to_test, classes))
    full_set_stats = analyze(flatten_list(backup_data), flatten_list(test_results), classes)
    # Compare classified data to original data.
    print_2d_array(full_set_stats)


def analyze(dat_old, dat_learned, input_classes):
    confusion = sa.confusion_matrix(dat_old, dat_learned, input_classes)
    confusion_totals = sa.totals(confusion)
    print(confusion_totals)
    stats = sa.calculate_error(confusion_totals)
    abs_error = sa.absolute_error(dat_old, dat_learned)
    mean_square_error = sa.mean_square_error(dat_old, dat_learned)
    print("Absolute Error: " + str(abs_error))
    print("Mean Square Error: " + str(mean_square_error))
    return stats


# Begin printing methods
def print_3d_array(ls):
    for i in ls:
        for j in i:
            print(j)


def print_2d_array(ls):
    for i in ls:
        print(i)
# End printing methods


# The driver that runs our code.
def driver():
    global classes
    data = get_list('1', '?')
    classes = 6
    unscrambled_data = copy.copy(data)
    print("Untouched Data:")
    cross_validate(unscrambled_data)  # Does the ten fold cross validation
    print("Scrambled Data:")
    scrambled_cv(unscrambled_data)  # Does the ten fold cross validation but with scrambled attributes.


driver()
