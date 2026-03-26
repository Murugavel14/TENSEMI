num = int(input("Enter number: "))
p = (num // 100)%10
q = (num // 1000)%10
r = (p*10)+q
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, r):
        if r % i == 0:
            print("not Prime")
            break
    else:
        print("Prime")