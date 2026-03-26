def main():
    for i in range (101,1000):
        for j in range (2, i):
            if(i % j == 0):
                break
        break
    print(i)
if __name__ == "__main__":
    main()

