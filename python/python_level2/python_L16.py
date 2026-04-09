def main():
    x = int(input("Enter Number: "))
    sum = 0
    count = 0
    temp = x
    if temp == 0:
        count = 1
    else:
        while(temp > 0):
            div  = temp % 10
            temp = temp // 10
            sum = sum + div
            count += 1
    check = True
    if(x == 0 or x == 1):
        print("NOT Prime")
    elif x > 1:
        for i in range(2,x):
            if((x % i) == 0):
                check = False
                break
        if(check):
            if(sum == 14):
                print("Prime & Sum of Digits 14")
            else:
                print("Prime & But Sum of Digits is not 14")
        else:
            if(sum == 14):
                print("Not Prime & But Sum of Digits 14")
            else:
                print("Not Prime & Sum of Digits is not 14")
if __name__ == "__main__":
    main()
