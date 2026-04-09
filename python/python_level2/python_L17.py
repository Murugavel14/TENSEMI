def main():
    x = int(input("Enter Number: "))
    div = x // 10
    ten = div % 10
    first = x % 10
    sum = ((ten*10) + first)
    check = False
    if sum > 1:
        for i in range(2,sum):
            if((sum % i) == 0):
                check = True
                break
        if(check):
            print("Not Prime",sum)
        else:
            print("Prime",sum)
if __name__ == "__main__":
    main()
