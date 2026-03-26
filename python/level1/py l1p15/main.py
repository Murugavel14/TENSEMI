def main():
    x = int(input("Enter Number: "))
   # Your Code Here
    a=int(x/100)#first 2
    f=int(x%100)#last 2
    b=int(a%10)#3dig
    c=int(a/10)#4dig
    d=int(b*10)+c
    y=int(d*100)+f
    print(f"Result = {y}")
if __name__ == "__main__":
    main()