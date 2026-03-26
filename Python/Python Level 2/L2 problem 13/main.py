#Python Level 2 | Problem 13
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    total=0
    while x>0:
        #temp=x%10
        total=(total*10)+(x%10)
        x=x//10
    print(f"Result = {total}")
if __name__ == "__main__":
    main()