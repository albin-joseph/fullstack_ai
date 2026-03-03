#import entire module
import math
print("Square root of 16 is: ", math.sqrt(16))

#import specific function from module
from random import randint
print("Random number between 1 and 100: ", randint(1, 100))

#import module with alias
import datetime as dt
print("Current date and time: ", dt.datetime.now())