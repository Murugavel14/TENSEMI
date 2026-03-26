#Python Level 1 | Problem 14 
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    #y=((((x%10)*10)+(x//10))*10)+((x//10)//10)
    #y=((x%10)*10)+((x//10)10)+((x//10)//10)
    y=((x%10)*100)+(((x//10)%10)*10)+((x//10)//10)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()