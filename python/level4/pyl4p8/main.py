def main():
    x = int(input("Enter Number: "))
    y=int(x%10)#1
    z=int(x/10)#first3
    m=int(z%10)#10
    n=int(z/10)#first2
    o=int(n%10)#100
    p=int(n/10)#1000
    q=int(((y*10 + m)*10 + o)*10 +p)
   # Your Code Here
    print(f"Result = {q}")
if __name__ == "__main__":main()