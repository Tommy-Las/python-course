import csv
import matplotlib.pyplot as plt
import statistics as sta
import copy


def welcome():
    print("\n\n----------------------------------------------------------------------------------------------")
    print("\nThe purpose of this program is to read data from the Iris Flower Dataset CSV file.\nWe compute the average, min, max and standard deviation of each attribute of each specie.\n")
    print("----------------------------------------------------------------------------------------------")

# functions for min, max, mean, standard deviation


def get_min(values):
    return min(values)


def get_max(values):
    return max(values)


def get_mean(values):
    return sta.mean(values)


def get_stdev(values):
    return sta.stdev(values)

# do the mean, max, min, standard deviation for each species'atrtributes


def compute_stats(temp_dict):
    for key, value in temp_dict.items():
        for key1, value1 in value.items():
            value1["mean"] = get_mean(value1["values"])
            value1["min"] = get_min(value1["values"])
            value1["max"] = get_max(value1["values"])
            value1["sta_dev"] = get_stdev(value1["values"])


# normalize given list
# normalized_value = (x - min) / (max - min)
def normalize_list(data):
    # temporary list to hold new normalized values
    temp_list = []
    maximum = max(data)
    minimum = min(data)
    a_range = maximum - minimum

    for number in data:
        number = ((number - minimum) / a_range)
        temp_list.append(number)

    return temp_list

# print a table that shows the statistics for each specie


def pretty_print(iris_dict):

    for key in iris_dict.keys():
        print(f"\nStatistics for the {key} flower specie")
        print("----------------------------------------------------------------------------------------------")
        print("{:>}{:>19}{:>19}{:>19}{:>19}".format(
            "Attributes(cm):", "Petal Length", "Petal Width", "Sepal Length", "Sepal Width"))
        print("----------------------------------------------------------------------------------------------")
        print("{:>4}{:>28.2f}{:>19.2f}{:>19.2f}{:>19.2f}".format(
            "Mean:", iris_dict[key]["petal_length"]["mean"], iris_dict[key]["petal_width"]["mean"], iris_dict[key]["sepal_length"]["mean"], iris_dict[key]["sepal_width"]["mean"]))
        print("{:>4}{:>29.2f}{:>19.2f}{:>19.2f}{:>19.2f}".format(
            "Min:", iris_dict[key]["petal_length"]["min"], iris_dict[key]["petal_width"]["min"], iris_dict[key]["sepal_length"]["min"], iris_dict[key]["sepal_width"]["min"]))
        print("{:>4}{:>29.2f}{:>19.2f}{:>19.2f}{:>19.2f}".format(
            "Max:", iris_dict[key]["petal_length"]["max"], iris_dict[key]["petal_width"]["max"], iris_dict[key]["sepal_length"]["max"], iris_dict[key]["sepal_width"]["max"]))
        print("{:>4}{:>14.2f}{:>19.2f}{:>19.2f}{:>19.2f}".format(
            "Standard Deviation:", iris_dict[key]["petal_length"]["sta_dev"], iris_dict[key]["petal_width"]["sta_dev"], iris_dict[key]["sepal_length"]["sta_dev"], iris_dict[key]["sepal_width"]["sta_dev"]))
        print("----------------------------------------------------------------------------------------------")


# plot sepal_length vs sepal width for each specie
def plot_sepal(iris_dict):
    plt.scatter(iris_dict["setosa"]["sepal_length"]["values"],
                iris_dict["setosa"]["sepal_width"]["values"], c="dodgerblue", label="Setosa")
    plt.scatter(iris_dict["versicolor"]["sepal_length"]["values"],
                iris_dict["versicolor"]["sepal_width"]["values"], c="orange", label="Versicolor")
    plt.scatter(iris_dict["virginica"]["sepal_length"]["values"],
                iris_dict["virginica"]["sepal_width"]["values"], c="hotpink", label="Virginica")
    plt.legend()
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.title("Sepal Length vs Sepal Width Scatter Plot")
    plt.show()

# plot petal_length vs petal_width for each specie


def plot_petal(iris_dict):
    plt.scatter(iris_dict["setosa"]["petal_length"]["values"],
                iris_dict["setosa"]["petal_width"]["values"], c="dodgerblue", label="Setosa")
    plt.scatter(iris_dict["versicolor"]["petal_length"]["values"],
                iris_dict["versicolor"]["petal_width"]["values"], c="orange", label="Versicolor")
    plt.scatter(iris_dict["virginica"]["petal_length"]["values"],
                iris_dict["virginica"]["petal_width"]["values"], c="hotpink", label="Virginica")
    plt.legend()
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")
    plt.title("Petal Length vs Petal Width Scatter Plot")
    plt.show()

# decision tree classifier with given value


def do_tree(value):
    print("\n----------------------------------------------------------------------------------------------")
    print("{:>50}".format(f"DECISION TREE FOR PETAL WIDTH {value}cm"))
    print("----------------------------------------------------------------------------------------------")

    if(value >= 0.1 and value <= 2.50):
        if(0.1 <= value <= 0.6):
            print(
                f"If the pedal width is {value}cm, then it looks like is Setosa")
        elif(1 <= value < 1.40):
            print(
                f"If the pedal width is {value}cm, then it looks like is Versicolor")
        elif(1.40 <= value <= 1.80):
            print(
                f"If the pedal width is {value}cm, then it looks like is Versicolor or Virginica")
        else:  # value > 180
            print(
                f"If the pedal width is {value}cm, then it looks like is Virginica")
    else:
        print(
            f"No specie found with pedal width of {value}")


def main():
    welcome()

    # open file
    iris_file = open("iris.csv", 'r')
    # store data in dictionary
    iris_data = csv.DictReader(iris_file)

    # dictionary of dictionaries to hold the sums and count
    iris_dict = {"setosa": {"sepal_length": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0},
                            "sepal_width": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}, "petal_length": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}, "petal_width": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}},
                 "versicolor": {"sepal_length": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}, "sepal_width": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}, "petal_length": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}, "petal_width": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}},
                 "virginica": {"sepal_length": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}, "sepal_width": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}, "petal_length": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}, "petal_width": {"values": [], "mean": 0, "min": 0, "max": 0, "sta_dev": 0}}}

    # we add values into a list depending of the specie and attribute
    for line in iris_data:
        iris_dict[line["species"]
                  ]["sepal_length"]["values"].append(float(line["sepal_length"]))
        iris_dict[line["species"]]["sepal_width"]["values"].append(
            float(line["sepal_width"]))
        iris_dict[line["species"]
                  ]["petal_length"]["values"].append(float(line["petal_length"]))
        iris_dict[line["species"]]["petal_width"]["values"].append(
            float(line["petal_width"]))

    # compute mean, min, max, standard deviation for regular values
    compute_stats(iris_dict)

    print("\n----------------------------------------------------------------------------------------------")
    print("{:>60}".format("STATISTICS FOR REGULAR VALUES"))
    print("----------------------------------------------------------------------------------------------")
    pretty_print(iris_dict)

    # sepal_length vs sepal_width plot
    plot_sepal(iris_dict)

    # Petal_length vs Petal_width plot
    plot_petal(iris_dict)

    # make a DEEP copy to create a dictionary with normalized values
    normalized_dict = copy.deepcopy(iris_dict)

    # normalize values for each species attributes
    for key, value in normalized_dict.items():
        for key1, value1 in value.items():
            value1["values"] = normalize_list(value1["values"])

    # with normalized values, calculate statistics
    compute_stats(normalized_dict)

    # print table of normalized values
    print("\n----------------------------------------------------------------------------------------------")
    print("{:>60}".format("STATISTICS FOR NORMALIZED VALUES"))
    print("----------------------------------------------------------------------------------------------")
    pretty_print(normalized_dict)

    # decision trees for  different petal widths
    do_tree(0.4)
    do_tree(1.2)
    do_tree(1.4)
    do_tree(2)
    do_tree(4)

    print()


main()
