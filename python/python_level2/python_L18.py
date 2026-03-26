def main():
    x = int(input("Enter Number: "))
    hun_div = x // 100
    hund = hun_div % 10
    div = x // 10
    ten = div % 10
    sum = ((hund*10) + ten)
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

