def main():
    for i in range (101,1000):
        pc = True
        for j in range (2, i):
            if(i % j == 0):
                pc = False
                break
        if pc:
            y = i
    print(y)
if __name__ == "__main__":
    main()
