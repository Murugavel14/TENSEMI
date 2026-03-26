x = int(input("Enter the Number: "))
n = x
rev = 0
while (n>0):
    z = n %10
    rev = (rev*10)+z
    n = n// 10
print (rev)