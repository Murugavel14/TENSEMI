#Python Level 1 | Problem 15
def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    # y=((x%10)*1000)+((((x//10)//10)%10)*100)+(((((x//10)//10)//10)%10)*10)+((x//10)//10)
    
    #y=((x%10)*1000)+(((x//10)%10)*100)+(((x//100)%10)*10)+(x//1000)
    y=((x//100)*100)+(((x%10)*10))+(x//10)%10
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
