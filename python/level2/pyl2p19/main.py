def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    a=int(x/10)#first 3
    b=int(a%10)#10's
    c=int(a/10)%10#100's
    d=int(c*10 + b)
    count=0
    for i in range(1,d+1):
      if(d%i==0):
        count=count+1
    if(count==2):
      print("prime")
    else:
      print("not prime")
if __name__ == "__main__":
    main()