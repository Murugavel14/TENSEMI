#Python Level 1 | Problem 27
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    if((x//100)+((x//10)%10)+(x%10)==10):
        y="Success"
    else:
        y="Failure"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()