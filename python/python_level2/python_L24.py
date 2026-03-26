def main():
    x = int(input("Enter Number: "))
    count = 0
    temp = x
    while(temp > 0):
        div  = temp % 10
        temp = temp // 10
        if div in (2, 3, 5, 7):
            count += 1
    print(count)
if __name__ == "__main__":
    main()
