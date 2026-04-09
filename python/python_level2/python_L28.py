def main():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    big = max(a,b,c)
    while True:
        if((big % a) == 0 and (big % b) == 0 and (big % c) == 0):
            print(big)
            break
        big += 1
if __name__ == "__main__":
    main()
