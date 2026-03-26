def main():
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    first = (num1 // 100)
    second = (num2 // 100)
    y = (first - second)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
