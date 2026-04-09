x = int (input("enter the number: "))
sumofdigit = 0
while (x >0):
    sumofdigit += x % 10
    x = x // 10
print (sumofdigit)