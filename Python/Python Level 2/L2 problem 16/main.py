#Python Level 2 | Problem 16
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    count=0
    for i in range(1,x+1):
        if(x%i==0):
            count=count+1
    if(count==2):
        y="prime"
    else:
        y="not prime"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()