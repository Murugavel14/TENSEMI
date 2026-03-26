#Python Level 4 | Problem 31 
def main():
   # x = int(input("Enter Number: "))
   # Your Code Here
    count=0
    for i in range(0,1000+1):
        while(i>0):
            rem=i%10 
            if(rem==0):
                count+=1
            i//=10
    print(f"Result = {count}")
if __name__ == "__main__":
    main()