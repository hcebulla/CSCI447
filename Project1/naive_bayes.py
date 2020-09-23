# This is our implementation of Naive Bayes
# Jordan Kelly, Hannah Cebulla, and Ryan Pallman
import random

number_of_examples = 0
frequency_table = []


def make_table(data_list):
    global frequency_table, number_of_examples

    for row in range(len(data_list)):  # Run through input data

        class_type = data_list[row][len(data_list[row])-1]  # Class of current row.
        class_index = -1  # Index of the class in the frequency table.

        for frequency_table_row in range(len(frequency_table)):  # Check for a class that already exists.
            if class_type == frequency_table[frequency_table_row][len(frequency_table[frequency_table_row])-2]:
                # If the class is in the table then store the index in class_index
                class_index = frequency_table_row

        if class_index == -1:  # Checking to see if there is already a class otherwise it will make a new one.
            frequency_table.append([])
            for elem in range(len(data_list[row])-1):
                if data_list[row][elem] == "$":
                    frequency_table[len(frequency_table)-1].append([])
                    continue
                frequency_table[len(frequency_table)-1].append([[data_list[row][elem], 1]])
            frequency_table[len(frequency_table) - 1].append(data_list[row][len(data_list[row]) - 1])
            frequency_table[len(frequency_table) - 1].append([1])
            number_of_examples += 1
            continue

        # We've found a match in our frequency table!
        for attr in range(len(data_list[row])-1):
            if data_list[row][attr] == "$":
                continue
            attribute = data_list[row][attr]
            attribute_index = -1
            for a in range(len(frequency_table[class_index][attr])):
                if attribute == frequency_table[class_index][attr][a][0]:
                    frequency_table[class_index][attr][a][1] += 1
                    attribute_index = a
            if attribute_index == -1:
                frequency_table[class_index][attr].append([attribute, 1])

        frequency_table[class_index][len(frequency_table[class_index])-1][0] += 1
        number_of_examples += 1


def calculate_q():  # Calculate Q -- we take the number of examples of a class divided by the count of examples.

    global frequency_table

    for row in range(len(frequency_table)):
        frequency_table[row][len(frequency_table[row])-1].append(frequency_table[row][len(frequency_table[row])-1][0]/number_of_examples)  # append Q to the class total


def calculate_f():  # Calculate F -- we calculate the relative percentage for every attribute.

    global frequency_table

    for row in range(len(frequency_table)):
        number_attribute = len(frequency_table[row])-2
        for attr in range(number_attribute):
            for value in range(len(frequency_table[row][attr])):
                numerator = 1 + frequency_table[row][attr][value][1]
                denominator = number_attribute + frequency_table[row][len(frequency_table[row])-1][0]
                frequency_table[row][attr][value].append((numerator/denominator))


def train(data_list):
    # We're using a four dimensional list with the following dimensions:
    # Our outermost is "class" followed by attribute, the value of the attribute, and finally the total

    make_table(data_list)
    calculate_q()
    calculate_f()


def classify(data_list):  # Classify data that is passed in without a class.
    global frequency_table

    for row in range(len(data_list)):
        class_chances = []
        for row_class in range(len(frequency_table)):
            chance_c = frequency_table[row_class][len(frequency_table[row_class])-1][1]
            for attr in range(len(data_list[row])):
                if "$" == data_list[row][attr]:
                    continue
                value_found = False
                for value in range(len(frequency_table[row_class][attr])):
                    if data_list[row][attr] == frequency_table[row_class][attr][value][0]:
                        chance_c *= frequency_table[row_class][attr][value][2]
                        value_found = True
                        break
                if not value_found:
                    chance_c = 0
                    break
            class_chances.append(chance_c)
        ma = max(class_chances)
        if ma == 0:
            rc = random.randint(0, len(frequency_table)-1)
            data_list[row].append(frequency_table[rc][len(frequency_table[rc])-2])
        else:
            for c in range(len(class_chances)):
                if class_chances[c] == ma:
                    data_list[row].append(frequency_table[c][len(frequency_table[c])-2])

    return data_list
