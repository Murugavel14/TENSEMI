def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    pcount=0
    for i in range(10,100):
      count=0
      for j in range(1,i+1):
        if(i%j==0):
          count=count+1
      if(count==2):
        pcount=pcount+1
    print(f"Result = {pcount}")
if __name__ == "__main__":
    main()