x = int(input("Enter Number: "))
p = (x // 10) % 10
y = x - 5 * (p % 2)
print(f"Result = {y}")
