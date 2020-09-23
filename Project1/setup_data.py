# This file reads and interprets our data so we can use it in other parts of our program.
# Jordan Kelly, Hannah Cebulla, and Ryan Pallman
import os  # Needed for file paths.

dirname = os.path.dirname(__file__)  # Current Folder
filepath = os.path.join(dirname, 'Datasets/')  # Datasets folder


def load_data(fileNum, missing_value_char):
    output = []
    datasets = ["breast-cancer-wisconsin.data", "glass.data", "house-votes-84.data", "iris.data", "soybean-small.data"]

    fileToOpen = filepath + datasets[int(fileNum) - 1]  # creates file path to numbered data file numbered naturally 1-5

    fileIn = open(fileToOpen, "r")
    numRemoved = 0

    for line in fileIn.readlines():
        if line != "": # If line is not empty then
            output.append([])  # Create a list for a new point of data
            for iter in line.split(","):  # Separate the data points
                iter = iter.rstrip()  # Remove new line character
                if iter == missing_value_char:
                    output[-1].append("$") # Replace missing value
                elif iter.isdigit():  # Determine if the input is a number. If it is we're going to convert it into an integer.
                    output[-1].append(int(iter.rstrip()))
                else:
                    try:
                        output[-1].append(float(iter))  # If the input is a float keep it as a float.
                    except ValueError:
                        if iter != '':  # If it is not an integer or a float we're going to store it as a string.
                            output[-1].append(iter)
    output = [z for z in output if z != []]  # Remove last entry in the output since it might be a new line.
    for z in range(0, len(output[0])):
        strings = []  # Store all unique strings in a column.
        for y in range(0, len(output)):
            if isinstance(output[y][z], str) and output[y][z] != "$":
                repeat = False
                for x in range(0, len(strings)):
                    if output[y][z] == strings[x]:
                        repeat = True
                if not repeat:
                    strings.append(output[y][z])  # Check if the value is unique, if so: add to list
        strings.sort()
        if len(strings) > 0:
            for y in range(0, len(output)):
                for x in range(0, len(strings)):
                    if output[y][z] == strings[x]:
                        output[y][z] = x
            print("Column #", z + 1, " has been normalized")  # Here we're printing our what the numbers mean for clarity.
            for y in range(0, len(strings)):
                print(y, " = ", strings[y])

    print(fileNum)
    if fileNum == '1':
        for z in output:
            del z[0]
    elif fileNum == '5':
        for z in output:
            z.insert(17, z.pop(0))
    elif fileNum == '2':
        for z in output:
            z[-1] = z[-1] - 1
    for z in range(len(output)):
        print(output[z])

    print("There were ", numRemoved, " data points removed.")

    return output


def dataset_selector():
    print(
        "Please select which set of data you would like to use."
        "\n 1: Breast Cancer Data"
        "\n 2: Glass Data"
        "\n 3: House Votes Data"
        "\n 4: Iris Data"
        "\n 5: Soybean Data")

    selection = input("Please type the corresponding number from the list above: ")
    missing_value_character = input("What value represents a missing value? ")
    load_data(selection, missing_value_character)


dataset_selector()
