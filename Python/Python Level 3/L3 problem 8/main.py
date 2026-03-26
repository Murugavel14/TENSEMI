#Python Level 3 | Problem 8
def check_assending(no):
# Your Program Here
    for i in range(0,len(no)-1):
        if(no[i]>no[i-1]):
            return 0
        return 1
def main():
    number = input("Enter a number: ")
    result=check_assending(number)
    if result:
        print("yes")
    else:
    print(result)
if __name__ == "__main__":
    main()