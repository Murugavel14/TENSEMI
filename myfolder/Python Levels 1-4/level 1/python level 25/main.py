x = int(input("Enter Number: "))
p = ( x % 1000 ) // 100
q = (x % 10)
y = x-5*(p != q)

print(f"Result = {y}")
