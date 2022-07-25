# Driver program for A8 - COP 4045
import math
from fractions import Fraction


class Shape(object):
    def __init__(self, area, perimeter, shape):
        self.shape = shape
        self.perimeter = area
        self.area = perimeter

    def __str__(self):
        return f"\nThe shape is {self.shape}\nPerimeter: {self.perimeter:.2f}\nArea: {self.area:.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.circle_area = math.pi * (self.radius**2)
        self.circle_perimeter = 2 * math.pi * self.radius
        # passing first argument area, second argument perimeter
        Shape.__init__(self, self.circle_area,
                       self.circle_perimeter, 'circle')


class Polygon(Shape):
    def __init__(self, area, perimeter, shape, num):
        self.shape = 'polygon'
        self.number_of_sides = num
        Shape.__init__(self, area, perimeter, shape)


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        if(side1 + side2 > side3 and side1 + side3 > side2 and side2+side3 > side1):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
            self.triangle_perimeter = self.side1 + self.side2 + self.side3
            # compute area without height, using Heron's formula
            self.s = self.triangle_perimeter/2
            self.triangle_area = math.sqrt(self.s*(self.s-self.side1)
                                           * (self.s-side2)*(self.s-side3))
            Polygon.__init__(self, self.triangle_area,
                             self.triangle_perimeter, 'triangle', 3)
        else:
            print(
                f"\nERROR: CANNOT CREATE TRIANGLE WITH SIDES {side1}, {side2}, {side3}")
            self.side1 = 0
            self.side2 = 0
            self.side3 = 0


class Rectangle(Polygon):
    def __init__(self, height, width):
        self.shape = 'rectangle'
        self.height = height
        self.width = width
        self.rectangle_perimeter = (self.height*2) + (self.width*2)
        self.rectangle_area = width * height
        Polygon.__init__(self, self.rectangle_area,
                         self.rectangle_area, 'rectangle', 4)


class Square(Polygon):
    def __init__(self, side):
        self.side = side
        self.square_perimeter = side * 4
        self.square_area = self.side ** 2
        Polygon.__init__(self, self.square_area,
                         self.square_perimeter, 'square', 4)


class Pentagon(Polygon):
    def __init__(self, side):
        self.side = side
        self.pentagon_perimeter = self.side * 5
        self.pentagon_area = Fraction(1/4) * math.sqrt(5 *
                                                       (5 + (2 * math.sqrt(5)))) * (self.side ** 2)
        Polygon.__init__(self, self.pentagon_area,
                         self.pentagon_perimeter, 'pentagon', 5)


class Hexagon(Polygon):
    def __init__(self, side):
        self.side = side
        self.hexagon_perimeter = self.side * 6
        self.hexagon_area = ((3 * math.sqrt(3)) / 2) * (self.side ** 2)
        Polygon.__init__(self, self.hexagon_area,
                         self.hexagon_perimeter, 'polygon', 6)

# Create variables


my_circle = Circle(2)
# create a circle of radius = 2

my_triangle = Triangle(3, 1.7, 4.9)
# attempt to create a triangle with "incorrect" values
# should produce error message

my_triangle = Triangle(3, 7, 4.6)
# create a triangle passing the length of each side

my_rectangle = Rectangle(3, 4.5)
# create a rectangle of sides 3 and 4.5

my_square = Square(4)
# # create a square with sides of equal length

my_pentagon = Pentagon(3)
# # create a pentagon with sides of equal length

my_hexagon = Hexagon(3)
# create a hexagon with sides of equal length

############################################

# Print area and perimeter for each variable

print(
    f"\nFor my_circle:\nArea: {my_circle.area:.2f}\nPerimeter: {my_circle.perimeter:.2f}")
print(
    f"\nFor my_triangle:\nArea: {my_triangle.area:.2f}\nPerimeter: {my_triangle.perimeter:.2f}")
print(
    f"\nFor my_rectangle:\nArea: {my_rectangle.area:.2f}\nPerimeter: {my_rectangle.perimeter:.2f}")
print(
    f"\nFor my_square:\nArea: {my_square.area:.2f}\nPerimeter: {my_square.perimeter:.2f}")
print(
    f"\nFor my_pentagon:\nArea: {my_pentagon.area:.2f}\nPerimeter: {my_pentagon.perimeter:.2f}")
print(
    f"\nFor my_hexagon:\nArea: {my_hexagon.area:.2f}\nPerimeter: {my_hexagon.perimeter:.2f}")

# TO TEST STRING REPRESENTATION
# print(my_circle)
# print(my_triangle)
# print(my_rectangle)
# print(my_square)
# print(my_pentagon)
# print(my_hexagon)
