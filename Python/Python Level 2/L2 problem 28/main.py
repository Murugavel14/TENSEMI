#Python Level 2 | Problem 28
def main():
   # Your Code Here
    a=int(input("Enter no. 1:"))
    b=int(input("Enter no. 2:"))
    bigger=max(a,b)
    while True:
        if(bigger%a==0 and bigger%b==0):
            lcm=bigger
            break
        bigger+=1 
    print(lcm)
if __name__ == "__main__":
    main()