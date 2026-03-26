#Python Level 4 | Problem 35
def main():
    x =int(input("Enter Number 1:"))
    y =int(input("Enter Number 2:"))
   # Your Code Here
    big=max(x,y)
    while True:
        if(big%x==0 and big%y==0):
            lcm=big
            break
        big+=1 
    print("LCM:",lcm)
if __name__ == "__main__":
    main()