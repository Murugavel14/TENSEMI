def main():
    x = int(input("Enter Number: "))
    a = x // 10
    y = ((x % 10) * 100) + ((a % 10) * 10) + (x // 100)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()


