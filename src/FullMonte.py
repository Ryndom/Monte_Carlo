"""
Estimating pi by comparing number of random dots within
a circle that is inscribed within a square
"""
from random import random

# define t as number of dots
t = 10**8


"""
sudo code
1) generate random point x and y
2) check to see if point is within 1 unit from center
3) if it is add a unit to within
4) go back and generate another point
"""
def getpi(t):
    # define within as number within the circle
    within = 0

    for i in range(t):
        x, y = random(), random()
        # dist is the distance from 0 to point (x,y)
        dist = (x**2 + y**2)**(1/2)
        if dist < 1: # if point within circle
            within += 1

    mypi = 4 * within / t
    print (' my estimate for pi is: ', mypi)

if __name__ == '__main__':
    getpi(t)
