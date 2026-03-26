#Python Level 2 | Problem 19
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    count=0
    a=(((x//100)%10)*10)+((x//10)%10)
    for i in range(1,a+1):
        if(a%i==0):
            count=count+1
    if(count==2):
        y="prime"
    else:
        y="not prime"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()