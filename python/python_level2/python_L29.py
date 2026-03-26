def main():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    mini = min(a,b)
    while True:
        if((a % mini) == 0 and (b % mini) == 0): 
            print(mini)
            break
        mini -= 1
if __name__ == "__main__":
    main()


