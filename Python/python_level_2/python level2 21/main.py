x = int(input("enter the number: "))
count = 0
n = x
while (n > 0):
    digit = n%10
    if digit % 2 == 1:
        count += 1
    n = n//10
print (count)