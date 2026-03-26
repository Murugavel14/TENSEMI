x = int(input("Enter Number: "))
p = x % 10
q = x // 10
if (p + q) == 10:
    y = "success"
else:
    y = "failure"
print (f"Result = {y}")
