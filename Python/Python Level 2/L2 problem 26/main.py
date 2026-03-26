#Python Level 2 | Problem 26
def main():
   # Your Code Here
    bigger=0
    #for i in range(9999,999,-1):
    for i in range(1000,10000):
        if(i%7==0 and i%9==0):
            #previous=bigger
            bigger=i;
            #break
    print(bigger)
if __name__ == "__main__":
    main()