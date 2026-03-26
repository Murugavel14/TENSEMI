#Python Level 4 | Problem 20 
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    pcount=0
    for i in range(1,10):
        count=0
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count==2):
            print(i)
            pcount+=1
    print("Result:",pcount)
if __name__ == "__main__":
    main()