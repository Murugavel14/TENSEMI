#Python Level 1 | Problem 31
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    a=(x//100)+((x//10)%10)+(x%10)
    if(a>9):
        b=(a//10)+(a%10)
        if(b>9):
            y=(b//10)+(b%10)
        else:
            y=b;
    else:
        y=a
    print(f"Result = {y}")
if __name__ == "__main__":
    main()