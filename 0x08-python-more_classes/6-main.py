#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_1.number_of_instances = 10
print(my_rectangle_1)

print("{:d} is my_rectangle_1.number_of_instances".format(my_rectangle_1.number_of_instances))
my_rectangle_2 = Rectangle(2, 4)

print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

print("****************{:d} instances of Rectangle".format(my_rectangle_2.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
