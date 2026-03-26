def main():
    x = int(input("Enter Number: "))
    z=(x//10) % 10
    a=(x%10) * 10
    y=z + a
    print(f"Result = {y}")
if __name__ == "__main__":
    main()

