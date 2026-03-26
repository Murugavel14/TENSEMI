def main():
    x = int(input("Enter Number: "))
    a = x // 10
    b = (x // 100)
    y = ((x % 10) * 1000) + ((a % 10) * 100) + ((b % 10) * 10) + (x // 1000) 
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
