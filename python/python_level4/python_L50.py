def main():
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    result = [0] * 50
    result.append(num1 + num2)
    print(f"Result = {result}")
if __name__ == "__main__":
    main()
