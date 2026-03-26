#python Level 2 | Problem 7
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    sum=0
    for i in range(10,x+1):
        total=((i//10)+(i%10))
        if total==7 and i%2!=0:
           # y=total
            y=i
            print(f"Result = {y}")
if __name__ == "__main__":
    main()