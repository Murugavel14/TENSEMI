#Python Level 4 | Problem 33
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    
    count=0
    for i in range(1000,10000):
        dec=1
        n=str(i)
        for j in range(0,len(n)-1):
            if (n[j]>n[j+1]):
                dec=0 
                break
        if(dec==1):
            count+=1
    print(f"Result = {count}")
if __name__ == "__main__":
    main()
