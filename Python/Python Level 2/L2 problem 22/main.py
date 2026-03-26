#Python Level 2 | Problem 22
def main():
    x = int(input("Enter Number: "))
    count = 0

    while(x >= 10):
        rem = x % 100
        if(rem % 2 != 0):
            count += 1
            print(rem)
        x = x // 10

    print(f"Result = {count}")

if __name__ == "__main__":
    main()