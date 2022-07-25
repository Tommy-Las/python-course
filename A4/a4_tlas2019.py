
# Name: Tommy las Date: 06/17/21
# ASSIGNMENT 4: FUEL CONSUMPTION

import csv
import pylab

# Function that displays information about the program. Asks the user to pick option 1 or 2


def display_menu():
    print('''
    
    The purpose of this program is to read data from csv files, that contain information fuel economy info about cars.
    There is two options.
    The first option asks the user for an MPG Interval and displays make and model of car between that range.
    Second option asks the user to choose City, Highway or Overall MPG, and it will display trends over the years''')

    user_choice = input(
        "\nWould you like to get Mileage Info (1) or Trend Plot (2)?:  ")
    return int(user_choice)

# Ask user for intervals in option 1


def get_intervals():
    interval_string = input(
        "Enter MPG Interval(Two numbers separated by a space):")
    interval_min, interval_max = interval_string.split()
    return interval_min, interval_max


def display_data(min_interval, max_interval):
    a_file = open("epadata2015.csv", 'r')
    # Skip fist line in data (NO IMPORTANT)
    firstline = a_file.readline()
    data = csv.reader(a_file)
    # list that will contain tuples of car
    range_list = []
    for line in data:
        # if it is a car and is between the range (inclusive)
        if line[70] == 'car' and (min_interval <= line[10] <= max_interval):
            # add tuple to range_list
            range_list.append((line[2], line[3]))
    print("Make\tModel")
    # display each car tuple from the range_list
    for car_tuple in range_list:
        print(f"{car_tuple[0]}, {car_tuple[1]}")


def get_mpg_info(mpg):
    if mpg == 'H':
        index = int(6)
        name = "Highway"
    elif mpg == 'C':
        index = int(5)
        name = "City"
    elif mpg == 'O':
        index = int(4)
        name = "Overall"
    return index, name


def do_graph(x, y, name, format):
    pylab.plot(x, y)
    pylab.xlabel("Year")
    pylab.ylabel(f"{name} MPG")
    pylab.title(f"{name} MPG over the years")

    if(format == "F"):
        pylab.savefig(f"{name}MPG_graph.png")
        print("\nSUCCESFUL: FILE WAS SAVED")
    else:
        pylab.show()


def create_graph(mpg, graph_format):
    a_file = open("epadata2020.csv", 'r')
    firstline = a_file.readline()
    data = csv.reader(a_file)
    x = []
    y = []

    index, name = get_mpg_info(mpg)

    # add values to x and y
    for line in data:
        x.append(int(line[0]))
        y.append(float(line[index]))

    do_graph(x, y, name, graph_format)


def main():

    user_choice = display_menu()

    if user_choice == 1:
        interval_min, interval_max = get_intervals()
        display_data(interval_min, interval_max)
    elif user_choice == 2:
        mpg = input(
            "Would you like to measure Highway MPG (H), City MPG (C) or Overall MPG (O): ").lower()

        graph_format = input(
            "Would you like to display the plot on screen (D) or save it as a file (F)? ").lower()
        if((mpg == 'h' or mpg == 'c' or mpg == 'o') and (graph_format == 'd' or graph_format == 'f')):
            create_graph(mpg.upper(), graph_format.upper())
        else:
            print("\nERROR: WRONG CHOICE")

    else:
        print("ERROR: Wrong choice")

    print("\nThank you for using my program!")


main()
