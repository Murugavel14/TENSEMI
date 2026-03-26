#Python Level 4 | Problem 32
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    count=0
    for i in range(1,1000000):
        pcount=0
        #for j in range(2,int(i**0.5)+1):
        for j in range(1,i+1):
            if(i%j==0):
                pcount+=1 
        if(pcount==2):
            total=0
            num=i
            while(num>0):
                total+=(num%10)
                num//=10
            if(total==14):
                count+=1
                print(i)
    print(f"Result = {count}")
if __name__ == "__main__":
    main()