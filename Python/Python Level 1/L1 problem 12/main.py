#Python Level 1 | Problem 12
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    y=(x%10)+((x//10)%10)+(((x//10))//10)
   # y=(x%10)+((x//10)%10)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()