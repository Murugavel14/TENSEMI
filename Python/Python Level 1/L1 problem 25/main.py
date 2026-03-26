#Python Level 1 | Problem 25 
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    #y=x-(5*((x//10)%10)==((x//100)%10))
    y=x-(5*(((x//10)%10)==((x//100)%10)))
    print(f"Result = {y}")
if __name__ == "__main__":
    main()