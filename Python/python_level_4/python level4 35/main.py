x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

a = max(x, y)
while True:
    if((a%x == 0) and (a%y == 0)):
        print(a)
        break
    a += 1