x = int(input("Enter Number: "))
y = int(input("enter the number: "))
p = (x // 100) + (x % 10)
q = (y // 100) + (y % 10)
if (p > q):
    z = p + (x // 10)%10
else:
    z = q + (y // 10)%10

print(f"Result = {z}")
