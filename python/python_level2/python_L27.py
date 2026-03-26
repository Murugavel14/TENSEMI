def main():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    big = max(a,b)
    while True:
        if(big % a == 0 & big % b == 0):
            print(big)
            break
        big += 1
if __name__ == "__main__":
    main()
