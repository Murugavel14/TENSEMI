#Python Level 2 | Problem 27 
def main():
   # Your Code Here
    count=0
    for num in range(1,100000):
        i=num
        total=0
        while(i>0):
            total=total+(i%10)
            i=i//10
        if(total==14):
            count+=1
            #print(i)
    print(count)
if __name__ == "__main__":
    main()