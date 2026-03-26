#Python Level 1 | Problem 35 
def main():
    x1 = int(input("Enter Number: "))
    x2 = int(input("Enter Number: "))
   # Your Code Here
    a=(x1//100)+(x1%10)
    b=(x2//100)+(x2%10)
    if(a>b):
        y=(x1//100)+((x1//10)%10)+(x1%10)
    else:
        y=(x2//100)+((x2//10)%10)+(x2%10)
    
    print(f"Result = {y}")
if __name__ == "__main__":
    main()