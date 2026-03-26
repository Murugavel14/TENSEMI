x = int(input("Enter Number: "))
f = (x % 100)
p = (x // 100)
q = (f // 10)
r = (f % 10)
z = p + q + r
if (z >= 10):
    if ( z == 19):
        y = ((z//10)+(z%10))//10
    else:
        y = ((z//10)+(z%10))
else:
    y = z

     
print(f"Result = {y}")
