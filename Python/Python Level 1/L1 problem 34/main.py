#Python Level 1 | Problem 34 
def main():
    x1= int(input("Enter Number: "))
    x2= int(input("Enter Number: "))
   # Your Code Here
    a=abs((x1//100)-(x1%10))
    b=abs((x2//100)-(x2%10))
    if(a>b):
        y=b
    else:
        y=a
    print(f"Result = {y}")
if __name__ == "__main__":
    main()