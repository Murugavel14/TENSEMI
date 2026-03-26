#Python Level 1 | Problem 21 
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    #y=(x%2==0)?(x-5):x
    y=x-(5*(x%2))
    print(f"Result = {y}")
if __name__ == "__main__":
    main()