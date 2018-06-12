#Read a group of values from command line args and print sum
from sys import argv
args = argv[1:]
sum = 0
for x in args:
    n = int(x)
    sum = sum + n

print("The sum of numbers = ", sum)