#Python Level 1 | Problem 32
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    a = int(input("Enter Number: "))
    if((x+a)<100):
        y=x+a
    else:
        b=x-a
        if(b<0):
            y=a-x
        else:
            y=b
    print(f"Result = {y}")
if __name__ == "__main__":
    main()