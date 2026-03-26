#Python Level 1 | Problem 29
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    if(((x//10)%10)+((x//100)%10)>10):
        y="Success"
    else:
        y="Failure"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()