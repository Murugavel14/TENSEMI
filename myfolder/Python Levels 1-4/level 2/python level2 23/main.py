x = int(input("enter the number: "))
count = 0
n = x
while (n > 0):
    digit = n%10
    if digit in (1, 4, 9):
       count += 1
    n = n//10
print (count)