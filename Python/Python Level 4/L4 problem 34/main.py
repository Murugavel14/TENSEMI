#Python Level 4 | Problem 34
def main():
    #x = int(input("Enter Number: "))
   # Your Code Here
    count=0
    for i in range(1,100000):
        y=i
        pal=0
        while(i>0):
            rem=i%10
            pal=(pal*10)+rem
            i//=10
        if(pal==y):
            print(y)
            count+=1
    print(count)
if __name__ == "__main__":
    main()