x = input("Enter the Number: ")
first = int(x[0])
rest = x[1:]
if (first % 2) != 0:
    first = first - 1
    y = str(first)+ rest
else:
    y = x
print (y)