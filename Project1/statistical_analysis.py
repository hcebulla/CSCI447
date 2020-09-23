# This file contains methods for comparing the data with the results.
# Jordan Kelly, Hannah Cebulla, and Ryan Pallman

import numpy
import setup_data
import copy
import random


# Calculate error via a confusion matrix.
def calculate_error(filled):
    error = numpy.full((5, len(filled) - 1), 0.0)
    for i in range(len(filled) - 1):
        fp = filled[i][-1] - filled[i][i]
        fn = filled[-1][i] - filled[i][i]
        tp = filled[i][i]
        error[3][i] = tp  # Correct values
        error[4][i] = fn + fp  # Incorrect values
        if (fp + fn + 2 * tp) != 0.0:
            error[0][i] = (fp + fn) / (fp + fn + 2 * tp)  # We're storing error here. We print this in the first row for each call.
        if (tp + fp) != 0.0:
            error[1][i] = tp / (tp + fp)  # We're storing precision here. We print this second in each call.
            print("Accuracy: " + str(error[1][i]))
        if (tp + fn) != 0.0:
            error[2][i] = tp / (tp + fn)  # We're storing recall here. We print this in the final row of each call.
    return error 


# Calculate totals in the confusion matrix.
def totals(confusion_matrix):
    class_number = len(confusion_matrix)
    result = numpy.full((class_number + 1, class_number + 1), 0)
    for i in range(class_number):
        for j in range(class_number):
            result[i][j] = confusion_matrix[i][j]
            result[i][-1] += confusion_matrix[i][j]
            result[-1][i] += confusion_matrix[j][i]
        result[-1][-1] += result[-1][i]
    return result


# Confusion matrix builder
def confusion_matrix(actual, predicted, num_of_classes):
    conf_matrix = numpy.full((num_of_classes, num_of_classes), 0)
    for i in range(len(actual)):
        conf_matrix[int(actual[i][-1])][int(predicted[i][-1])] += 1
    return conf_matrix


def mean_square_error(actual, predicted):
    result = 0
    for i in range(len(predicted)):
        result += pow((float(actual[i][-1]) - float(predicted[i][-1])), 2)
    result / len(predicted)
    return result


def absolute_error(actual, predicted):
    result = 0
    for i in range(len(predicted)):
        result += abs(float(actual[i][-1]) - float(predicted[i][-1]))
    return result
