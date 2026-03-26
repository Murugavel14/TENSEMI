#Python Level 3 | Problem 9 
def swapNumbers(no):
# Your Program Here
    last=no%10
    rev=last*10+(no//10)
    return rev
def main():
    number = int(input("Enter a number: "))
    result=swapNumbers(number)
    print(result)
if __name__ == "__main__":
    main()