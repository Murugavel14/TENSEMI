def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    a=int(x%10)
    b=int(x/10)%10
    c=int(b*10 + a)
    count=0
    for i in range(1,c+1):
      if(c%i==0):
        count=count+1
    if(count==2):
      print("prime")
    else:
      print("not prime")
if __name__ == "__main__":
    main()