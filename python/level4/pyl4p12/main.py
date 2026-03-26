def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    rev=0
    while x!=0:
   #for x in range(x,0,-1):
      y=int(x%10)
      rev=rev*10+y
      x=int(x/10) 
    print(f"Result = {rev}")
if __name__ == "__main__":main()