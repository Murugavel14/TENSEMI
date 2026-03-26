#Python Level 2 | Problem 24
def main():
    x = int(input("Enter Number: "))
    count = 0

    while x >= 10:
        rem = x % 100

        if rem==16 or rem==25 or rem==36 or rem==49 or rem==64 or rem==81:
            count += 1
            print(rem)

        x = x // 10

    print(f"Result = {count}")

if __name__ == "__main__":
    main()