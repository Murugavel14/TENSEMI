x = input("Enter the Number: ")
if len (x)>1:
    y = x [-1]+ x[1:-1]+x[0]
else:
    y = x
print (y)