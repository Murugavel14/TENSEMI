#Python Level 2 | Problem 21
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    #temp=x 
    oddcount=0
    while(x>0):
        rem=x%10
        if(rem%2!=0):
            oddcount+=1
        x=x//10
    y=oddcount
    print(f"Result = {y}")
if __name__ == "__main__":
    main()