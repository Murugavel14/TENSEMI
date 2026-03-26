#Python Level 2 | Problem 17 
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    count=0
    for i in range(1,x+1):
        if(x%i==0):
            count=count+1
    s=0
    while(x>0):
        s=s+(x%10)
        x=x//10
    if(count==2 and s==14):
        y="prime and sum is 14"
    elif (count!=2 and s==14):
        y="Not Prime but sum of digits is 14"
    else:
        y="Prime, but sum of Digits is not 14"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()