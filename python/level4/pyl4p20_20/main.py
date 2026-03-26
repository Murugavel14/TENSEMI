def main():
    #x = int(input("Enter Number: "))
    pcount=0
    for i in range(0,10):
      count=0
      for j in range(1,i+1):
        if(i%j==0):
         count=count+1
         print(i)
      if(count==2):
        pcount=pcount+1
        print(i)
   # Your Code Here
    print(f"Result = {pcount}")
if __name__ == "__main__":main()