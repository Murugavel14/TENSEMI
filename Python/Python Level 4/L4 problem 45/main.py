#Python Level 4 | Problem 45
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    rev=0
    while(x>0):
        rem=x%10
        rev=(rev*10)+rem
        x//=10
    print(f"Result = {rev}")
if __name__ == "__main__":
    main()