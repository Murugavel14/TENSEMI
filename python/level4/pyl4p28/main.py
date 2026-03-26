def main():
   # x = int(input("Enter Number: "))
   for i in range(1000,10000):
       count=0
       for j in range(1,i+1):
         if(i%j==0):
            count=count+1
       if(count==2):
         print(i)
         break
   # Your Code Here
    #print(f"Result = {y}")
if __name__ == "__main__":
    main()