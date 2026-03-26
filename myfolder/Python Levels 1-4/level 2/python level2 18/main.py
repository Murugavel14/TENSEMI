num = int(input("Enter number: "))
z = num % 100
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, z):
        if z % i == 0:
            print("not Prime")
            break
    else:
        print("Prime")