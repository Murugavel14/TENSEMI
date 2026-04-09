x = int(input("Enter the Number: "))
count = 0
n = x
while (n > 0):
      digit = n %10
      if digit in (2,3,5,7):
        count += 1 
      n = n//10
print(count)