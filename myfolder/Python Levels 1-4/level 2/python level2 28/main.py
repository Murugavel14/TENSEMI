x = int(input("Enter the Number: "))
y = int(input("Enter the Number: "))
gcd = max(x,y)
while True:
    if (gcd % x) == 0 and (gcd % y) == 0:
      print(gcd)
      break
    gcd += 1
