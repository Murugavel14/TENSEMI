#Python Level 1 | Problem 23 
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    #y=x-(5*((x//10)+(x%10))%2)
    y=x-(5*(((x//10)+(x%10))%2))
    print(f"Result = {y}")
if __name__ == "__main__":
    main()