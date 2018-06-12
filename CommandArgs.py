from sys import argv
print(type(argv))
print(argv)

#use slice till end
print(argv[1:])

#print only first command line arg
print(argv[1])

#begin:end:step
print(argv[0:3:1])

#full
print(argv[:])

#len function on array
print("The number of command line arguments including the name of the file: ", len(argv))

#print one by one
for x in argv:
    print(x)