import math
x=int(input("Enter a number: "))
count=0
while x>9:
    y=int(x%100)
    a=int(math.sqrt(y))
    b=int(a*a)
    if(b==y):
      count=count+1
    x=int(x/10)   # Remove last digit
print(count)