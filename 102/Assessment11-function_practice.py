# Grace Luka
# CSCI 102 - Section B
# Assesment 11
# References: www.w3schools.com for arctan function
# Time:

import math


# Problem 1 -------------------------------
def print_output(var):
    print(f'OUTPUT {var}')
    return

#var = input()


# Problem 2 ------------------------------

def cylinder_vol(radius, height):
    pi = 3.1415
    radius = float(radius)
    height = float(height)
    volume = (pi * (radius * radius) * height)
    return print_output(f'{volume:.2f}')

#radius = float(input())
#height = float(input())


# Problem 3 -----------------------------

def lbs_to_kg(pounds):
    kilograms = pounds * 0.4536
    return print_output(f'{kilograms:.4f}')

#pounds = int(input())


# Problem 4 -----------------------------

def polar_coords(x,y):
    r = math.sqrt((x**2) + (y**2))
    theta = math.degrees(math.atan(y / x))
    return print_output(f'r: {r:.2f}\nOUTPUT theta: {theta:.2f}')

#x = int(input())
#y = int(input())




# Problem 5 -----------------------------

def yen_to_dollars(yen):
    dollars = yen * 0.0068
    return print_output(f'{dollars:.2f}')

#yen = int(input())



# Problem 6 --------------------------------

def quad_form(a,b,c):
    answer1 = math.sqrt(((b**2)-(4*a*c)))
    answer1 = -b + answer1
    answer1 = int(answer1 / (2*a))
    answer2 = math.sqrt(((b**2)-(4*a*c)))
    answer2 = -b - answer2
    answer2 = int(answer2 / (2*a))
    if answer1 < answer2:
        return print_output(f'{answer1}\nOUTPUT {answer2}')
    else:
        return print_output(f'{answer2}\nOUTPUT {answer1}')


#a = int(input())
#b = int(input())
#c = int(input())

#print_output(quad_form(a,b,c))


