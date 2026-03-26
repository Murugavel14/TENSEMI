x = int(input("Enter Number: "))
z = int(input("enter the number: "))
a = x % 10
b = x// 10
c = z %10
d = z// 10
if ((a+b) > (c+d)):
   y = a+b
else:
    y = c+d
print(f"Result = {y}")
