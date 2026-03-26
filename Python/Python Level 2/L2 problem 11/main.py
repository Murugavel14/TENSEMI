#Python Level 2 | Problem 11
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    y=0
    #temp=x
    while x>0:
        x=x//10
        y=y+1
    print(f"Result = {y}")
if __name__ == "__main__":
    main()