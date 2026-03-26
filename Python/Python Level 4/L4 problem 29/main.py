#Python Level 4 | Problem 23
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    total=0
    for i in range(9999,999,-1):
        count=0
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count==2):
            print(i)
            break
            #total+=i
    #print("Result:",total)
if __name__ == "__main__":
    main()