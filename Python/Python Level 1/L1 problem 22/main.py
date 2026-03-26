#Python Level 1 | Problem 22 
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
   # y=x-((5*(x//10)%10)%2)
    y=x-(5*(((x//10)%10)%2))
    print(f"Result = {y}")
if __name__ == "__main__":
    main()