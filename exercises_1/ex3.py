# App to calculate the hypotenuse and the area of a right-angled triangle
# Write a console programme that
# (1) Allows users to enter two numbers as length of legs
# (2) Makes sure what users entered are valid
# (3) Calculated and prints the hypotenuse and the area of the triangle

import math

def get_info_triangle():
    try:
        print('Input length of the first side:')
        first_side_length = float(input())
        print('Input length of the second side:')
        second_side_length = float(input())
        print('The hypotenuse is', math.sqrt(first_side_length ** 2 + second_side_length ** 2))
        print('The area is', (first_side_length * second_side_length/2))
    except:
        print('Length of the side must be number!')
        get_info_triangle()

get_info_triangle()
