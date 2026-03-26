def main():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    big  = max(num1, num2)
    while True:
        if(big % num1 == 0 and big % num2 == 0):
            print(big)
            break
        big += 1
if __name__ == "__main__":
    main()    
