# Tommy Las, Z23517623, 06/27/2021, ASSIGNMENT 5
import csv


def welcome():
    print("\n----------------------------------------------------------------------")
    print("\nThe purpose of this program is to read data from the Iris Flower Dataset CSV file.\nWe compute the average of each attribute of each specie.\n")

# function that gets average from a given dictionary


def get_avg(a_dict):
    # I deep copy the dict, I think is the proper way, since it would modify the dict from main function too
    b_dict = a_dict.copy()

    # compute the averages
    b_dict["sepal_length"] /= b_dict["count"]
    b_dict["sepal_width"] /= b_dict["count"]
    b_dict["petal_length"] /= b_dict["count"]
    b_dict["petal_width"] /= b_dict["count"]

    # return tuple with averages
    return (b_dict["petal_length"],  b_dict["petal_width"],
            b_dict["sepal_length"],  b_dict["sepal_width"])

# function that displays data in an appealing way


def pretty_print(avg_dict):
    print("----------------------------------------------------------------------")
    print("{:>}{:>19}{:>19}{:>19}".format(
        "Species:", "Setosa", "Versicolor", "Virginica"))
    print("----------------------------------------------------------------------")
    print("Attributes (cm):")
    print(" {:>4}{:>9.2f}{:>18.2f}{:>18.2f}".format(
        "Avg petal length:", avg_dict["setosa"][0], avg_dict["versicolor"][0], avg_dict["virginica"][0]))
    print(" {:>4}{:>10.2f}{:>18.2f}{:>18.2f}".format(
        "Avg petal width:", avg_dict["setosa"][1], avg_dict["versicolor"][1], avg_dict["virginica"][1]))
    print(" {:>4}{:>9.2f}{:>18.2f}{:>18.2f}".format(
        "Avg sepal length:", avg_dict["setosa"][2], avg_dict["versicolor"][2], avg_dict["virginica"][2]))
    print(" {:>4}{:>10.2f}{:>18.2f}{:>18.2f}\n".format(
        "Avg sepal width:", avg_dict["setosa"][3], avg_dict["versicolor"][3], avg_dict["virginica"][3]))


def main():
    welcome()

    # open file
    iris_file = open("iris.csv", 'r')
    # store data in dictionary
    iris_data = csv.DictReader(iris_file)

    # dictionary of dictionaries to hold the sums and count
    sum_dict = {"setosa": {"sepal_length": 0,
                           "sepal_width": 0, "petal_length": 0, "petal_width": 0, "count": 0},
                "versicolor": {"sepal_length": 0, "sepal_width": 0, "petal_length": 0, "petal_width": 0, "count": 0},
                "virginica": {"sepal_length": 0, "sepal_width": 0, "petal_length": 0, "petal_width": 0, "count": 0}}

    # we add values to sum_dict depending on line["species"]
    for line in iris_data:
        sum_dict[line["species"]
                 ]["sepal_length"] += float(line["sepal_length"])
        sum_dict[line["species"]]["sepal_width"] += float(line["sepal_width"])
        sum_dict[line["species"]
                 ]["petal_length"] += float(line["petal_length"])
        sum_dict[line["species"]]["petal_width"] += float(line["petal_width"])
        sum_dict[line["species"]]["count"] += 1

    # get averages for each flower
    setosa_tuple = get_avg(sum_dict["setosa"])
    versicolor_tuple = get_avg(sum_dict["versicolor"])
    virginica_tuple = get_avg(sum_dict["virginica"])

    avg_dict = {"setosa": setosa_tuple,
                "versicolor": versicolor_tuple, "virginica": virginica_tuple}

    pretty_print(avg_dict)


main()
