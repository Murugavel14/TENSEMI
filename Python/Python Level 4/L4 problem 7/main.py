#Python Level 4 | Problem 7 
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    y=((x%10)*100)+(((x//10)%10)*10)+(x//100)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()