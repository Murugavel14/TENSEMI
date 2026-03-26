x = int(input("Enter Number: "))
p = x % 10
z = x // 10
r = z % 10
q = z // 10

if (p + q + r) == 10:
    y = "success"
else:
        y = "failure"
print (f"Result = {y}")