import csv


# preprocess the data sets
def loadfile(filename):

    reader = csv.reader(open(filename))
    data = list(reader)

    print(data)


def main():

    loadfile('breastCancer.csv')
    loadfile('iris.csv')
    loadfile('vote.csv')
    loadfile('soybean.csv')
    loadfile('glass.csv')


main()

