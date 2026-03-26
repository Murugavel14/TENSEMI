def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    sum=0
    while x!=0:
   #for x in range(x,0,-1):
      y=int(x%10)
      sum=sum+y
      x=int(x/10) 
    print(f"Result = {sum}")
if __name__ == "__main__":main()