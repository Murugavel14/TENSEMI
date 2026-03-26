#Python Level 2 | Problem 9
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
   y=0
    for i in range(10,x):
        if i%10==5:
            print(i)
            y=y+i
    print(f"Result = {y}")
if __name__ == "__main__":
    main()