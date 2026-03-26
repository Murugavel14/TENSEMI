#Python Level 2 | Problem 15
def main():
    x = input("Enter Number: ")
   # Your Code Here
    if int(x[-1])%2==0:
        y=x 
    else:
        y=str((int(x[0])-1))+(x[1:])
    print(f"Result = {y}")
if __name__ == "__main__":
    main()