def main():
    x = int(input("Enter Number: "))
    y = ((x % 10) * 10) + (x // 10)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
