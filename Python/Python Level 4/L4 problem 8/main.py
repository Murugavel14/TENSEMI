#Python Level 4 | Problem 8 
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    y=0
    while(x>0):
        y=(y*10)+(x%10)
        x=x//10
    print(f"Result = {y}")
if __name__ == "__main__":
    main()