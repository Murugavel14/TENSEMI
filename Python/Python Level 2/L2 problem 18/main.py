#Python Level 2 | Problem 18
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    count=0
    #for i in range(1,x+1):
    #while x!=0:
    a=(((x//10)%10)*10)+(x%10)
    for j in range(1,a+1):
        if a%j==0:
          count=count+1
    if count==2:
      y="Prime"
    else:
      y="Not prime"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()