#  With this concept of default parameters in mind, the goal of this assignment is to write a single function, 
#  randInt() that takes up to 2 arguments.

#  If no arguments are provided, the function should return a random integer between 0 and 100.
#  If only a max number is provided, the function should return a random integer between 0 and the max number.
#  If only a min number is provided, the function should return a random integer between the min number and 100
#  If both a min and max number are provided, the function should return a random integer between those 2 values. 
from random import random


def randInt(min=0,max=100):
    rand_num=round((random()*(max-min))+min)
    return rand_num

for i in range(100):
    print(randInt(min=5,max=-70))

# BONUS: account for any edge cases (eg. min > max, max < 0): what should be the behavior of the program in the edge cases?


