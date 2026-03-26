#Python Level 2 | Problem 20
def main():
   # x = int(input("Enter Number: "))
   # Your Code Here
    pcount=0
    for i in range(1,10):
        count=0
        for j in range(1,9+1):
            if(i%j==0):
                count+=1
        if(count==2):
            pcount+=1
            print(i)
    y=pcount
    print(f"Result = {y}")
if __name__ == "__main__":
    main()