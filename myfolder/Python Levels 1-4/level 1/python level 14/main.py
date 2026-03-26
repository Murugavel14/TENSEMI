x = int(input("Enter Number: "))
p = x % 100
q = x // 100
r = (p % 10) * 100
s = (p // 10) * 10
y = r + s + q
print(f"Result = {y}")