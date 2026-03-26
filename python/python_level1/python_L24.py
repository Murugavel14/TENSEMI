def main():
    x = int(input("Enter Number: "))
    first = (x // 100)
    five  = (first * 100)
    result = (five !=  500 and x) or x - 5
    y = result
    print(f"Result = {y}")
if __name__ == "__main__":
    main()

