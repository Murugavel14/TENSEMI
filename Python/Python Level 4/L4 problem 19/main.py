#Python Level 4 | Problem 19
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    y=0
    for i in range(100,1000):
        if(i%2!=0):
            print(i)
            y+=i
    print(f"Result = {y}")
if __name__ == "__main__":
    main()