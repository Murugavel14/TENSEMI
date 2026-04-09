def main():
    x = int(input("Enter Number: "))
    count = 0
    temp = x
    while(temp > 0):
        div  = temp % 100
        temp = temp // 10
        if div in (16, 25, 36, 49, 64, 81, 100):
            count += 1
    print(count)
if __name__ == "__main__":
    main()
