#Python Level 2 | Problem 14 
def main():
    x = input("Enter Number: ")
   # Your Code Here
    if len(x)>1:
        y=x[-1]+x[1:-1]+x[0]
    else:
        y=x
    print(f"Result = {y}")
if __name__ == "__main__":
    main()