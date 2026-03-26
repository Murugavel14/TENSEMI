x = int(input("Enter the Number: "))
y = int(input("Enter the Number: "))
gcd = min(x,y)
while gcd > 0:
    if (x%gcd == 0 and y%gcd == 0):
        print (gcd)
        break
    gcd -= 1 