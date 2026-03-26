x = int (input("Enter the Number: "))
y = int (input("Enter the Number: "))
z = int (input("Enter the Number: "))
gcd = max (x,y,z)

while True:
    if ((gcd%x == 0) & (gcd%y == 0) & (gcd%z == 0)):
        print(gcd)
        break
    gcd += 1