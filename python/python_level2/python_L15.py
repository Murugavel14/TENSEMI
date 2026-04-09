 (IT’S WORKS PROBERLY ON 2 DIGIT)
def main():
    x = int(input("Enter Number: "))
    check = 1
    for i in range(2,10):
        if(x % i == 0):
            check = 0
            break
        else:
            if(check == 0):
                check = 1
                if(x == 1):
                    check = 0
                    break
                break
    if(check == 1):
        y = "Prime"
    else:
        y = "Not"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
(Alternate but efficient)
def main():
    x = int(input("Enter Number: "))
    check = False
    if(x == 0 or x == 1):
        print("NOT Prime")
    elif x > 1:
        for i in range(2,x):
            if((x % i) == 0):
                check = True
                break
        if(check):
            print("Prime")
        else:
            print("Not Prime")
if __name__ == "__main__":
    main()
