x = int(input("enter the number: "))
count = 0
n = x
while (n > 9):
    digit = n%100
    if digit in (16, 25, 36, 49, 64, 81):
       count += 1
    n = n//10
print (count)