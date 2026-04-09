def main():
    x  = int(input("Enter Number: "))
    st = str(x)
    rev = st[::-1]
    count = 0
    for i in rev:
        count += 1
        if(i == 0):
            break
    temp = rev[0:count]
    print(temp[::-1])
if __name__ == "__main__":
    main()
