import turtle
import math


def output_purpose():
    print('This program will ask for 2 different coordinates from you. It will then draw a line from 0,0 to the 1st point,'
          'and from the 1st point to the second point. It will also calculate the acute (smaller) angle between the 2 lines')
    print()
    
def user_input():
    dictionary = {}
    for i in range (1,3):
        x_cord = int(input(f'Enter the x coordinate for point {i}: '))
        y_cord = int(input(f'Enter the y coordinate for point {i}: '))
        print()
        if x_cord not in dictionary:
            dictionary[i] = [x_cord,y_cord]
    return dictionary

def create_lines(dictionary):
    for i in range (1,3):
        point = turtle.goto(dictionary[i][0],dictionary[i][1])
        turtle.write(point)
    turtle.done()

def gradient1_calculation(dictionary):
    x1 = dictionary[1][0]
    y1 = dictionary[1][1]

    gradient1 = (y1-0)/(x1-0)
    print(f'The gradient between 0 and 1st point is {gradient1}')
    return gradient1

def gradient2_calculation(dictionary):
    x1 = dictionary[1][0]
    y1 = dictionary[1][1]

    x2 = dictionary[2][0]
    y2 = dictionary[2][1]

    gradient2 = (y2-y1)/(x2-x1)
    print(f'The gradient between 1st point and 2nd point is {gradient2}')
    return gradient2

def angle_calculations(gradient1, gradient2):
    m1 = gradient1
    m2 = gradient2
    tan_angle = (abs(m2-m1))/(1+m1*m2)
    radiant_angle = math.atan(tan_angle)
    angle = math.degrees(radiant_angle)
    print(f'The angle in radians is {radiant_angle}')
    print(f'The angle in degrees is {angle}')
    return angle
    

if __name__ == '__main__':
    output_purpose()
    dictionary = user_input()
    gradient1 = gradient1_calculation(dictionary)
    gradient2 = gradient2_calculation(dictionary)
    angle = angle_calculations(gradient1, gradient2)
