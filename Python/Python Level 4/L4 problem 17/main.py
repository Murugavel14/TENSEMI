#Python Level 4 | Problem 17
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    y=0
    for i in range(1,10):
        if(i%2!=0):
            print(i)
            y+=i
    print(f"Result = {y}")
if __name__ == "__main__":
    main()