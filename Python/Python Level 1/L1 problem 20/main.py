#Python Level 1 | Problem 20
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    y=((x//100)*100)+(x%10)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()