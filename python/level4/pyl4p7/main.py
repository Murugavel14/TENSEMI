def main():
    x = int(input("Enter Number: "))
    y=int(x%10)#1
    z=int(x/10)#first2
    m=int(z%10)#10
    n=int(z/10)#100
    o=int((y*10 + m)*10 + n)
   # Your Code Here
    print(f"Result = {o}")
if __name__ == "__main__":main()