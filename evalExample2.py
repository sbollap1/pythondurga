#eval will convert it to internal type
x = eval(input("Enter something: "))
print(type(x))

y = eval(input("Enter a list: "))

if (type(y) is list):
 for x1 in y:
   print(" Value: ", x1)
else:
    print("not supported")