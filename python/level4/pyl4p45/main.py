def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    rev=0
    while x>0:
        a=int(x%10)
        rev=int((rev*10)+a)
        x=int(x/10)
    print(f"Result = {rev}")
if __name__ == "__main__":main()