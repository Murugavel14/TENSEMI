#Python Level 4 | Problem 30
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    total=0
    for i in range(99999999,9999999,-1):
        count=0
        for j in range(2,((i+1)//2)+1):
            if(i%j==0):
                count+=1
        if(count==0):
            print(i)
            break
            #total+=i
    #print("Result:",total)
if __name__ == "__main__":
    main()