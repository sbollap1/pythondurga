#if you use argv[200] and its not there you will get error. but if you use slice you won't
from sys import argv

print(int(argv[1]) + int(argv[2]))