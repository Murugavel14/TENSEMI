def main():
    x = int(input("Enter Number: "))
    count = 0
    temp = x
    while(temp > 0):
        div  = temp % 100
        temp = temp // 10
        if((div % 2) != 0) & (div > 10):
            count += 1
    print(count)
if __name__ == "__main__":
    main()
