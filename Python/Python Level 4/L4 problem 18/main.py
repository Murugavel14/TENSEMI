#Python Level 4 | Problem 18
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    y=0
    for i in range(10,100):
        if(i%2!=0):
            print(i)
            y+=i
    print(f"Result = {y}")
if __name__ == "__main__":
    main()