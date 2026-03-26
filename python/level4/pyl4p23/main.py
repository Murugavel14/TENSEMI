def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    sump=0
    for i in range(0,10):
      count=0
      for j in range(1,i+1):
        if(i%j==0):
          count=count+1
      if(count==2):
        sump=sump+i
    print(f"Result = {sump}")
if __name__ == "__main__":
    main()