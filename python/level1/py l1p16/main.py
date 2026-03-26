def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    a=int(x/100)#first 2
    f=int(x%100)#last 2
    b=int(f%10)#1dig
    c=int(f/10)#2dig
    d=int(b*10)+c
    y=int(a*100)+d
    print(f"Result = {y}")
if __name__ == "__main__":
    main()