def main():
    add = 0
    for i in range (101,1000):
        pc = True
        for j in range (2, i):
            if(i % j == 0):
                pc = False
                break
        if pc:
            add += i
    print(add)
if __name__ == "__main__":
    main()
