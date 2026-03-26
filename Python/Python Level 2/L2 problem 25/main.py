#Python Level 2 | Problem 25
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    
    pcount=0
    while(x>0):
        rem=x%10
        count=0
        for i in range(1,rem+1):
            if(rem%i==0):
                count+=1
        if(count==2):
            pcount+=1
            print(i)
        x=x//10
        y=pcount
    print(f"Result = {y}")
if __name__ == "__main__":
    main()