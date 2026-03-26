def main():
   # x = int(input("Enter Number: "))
   for i in range(100000000,10000000,-1):
       count=0
       for j in range(1,int((i+1)/2)):
         if(i%j==0):
            count=count+1
       if(count==1):
         print(i)
         break
   # Your Code Here
    #print(f"Result = {y}")
if __name__ == "__main__":
    main()