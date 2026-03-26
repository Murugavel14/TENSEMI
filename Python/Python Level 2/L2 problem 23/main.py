#Python Level 2 | Problem 23
def main():
    x = int(input("Enter Number: "))
    count = 0

    while x > 0:
        rem = x % 10
        
        if rem == 1 or rem == 4 or rem == 9:
            count += 1
            print(rem)
        
        x = x // 10

    print(f"Result = {count}")

if __name__ == "__main__":
    main()