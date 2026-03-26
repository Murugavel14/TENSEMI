#Python Level 1 | Problem 33
def main():
    x1= int(input("Enter Number: "))
    x2= int(input("Enter Number: "))
   # Your Code Here
    if(x1>x2):
        y=(x1//10)+(x1%10)
    else:
        y=(x2//10)+(x2%10)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()