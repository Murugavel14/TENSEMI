#Python Level 4 | Problem 16
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    y=0
    for i in range(100,1000):
        if(i%2!=0):
            y+=1
    print(f"Result = {y}")
if __name__ == "__main__":
    main()