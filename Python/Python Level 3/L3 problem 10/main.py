#Python Level 3 | Problem 10 
def count_Digits(no):
# Your Program Here
    count=0
    while(no>0):
        rem=no%10
        count+=1 
        no//=10
    return count
def main():
    number1 = int(input("Enter a number: "))
    result=count_Digits(number1)
    print(result)
if __name__ == "__main__":
    main()