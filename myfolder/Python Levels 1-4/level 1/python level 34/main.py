x = int(input("Enter Number: "))
y = int(input("enter the number: "))
p = (x // 10)%10
q = (y // 10)%10
if (p > q):
   z = abs((x // 100) - (x % 10))
else:
    z = abs ((y // 100) - (y % 10))

print(f"Result = {z}")
