def main():
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    add  = num1 + num2
    if(100 < add):
        y = num1 - num2
    else:
        y = add
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
