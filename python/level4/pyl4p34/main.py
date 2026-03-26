def main():
    count=0
    for i in range(0,100000):
        x=i
        rev=0
        while x>0:
          a=int(x%10)#1
          rev=int((rev*10)+a)
          x=int(x/10)
        if(i==rev):
          count=count+1
    print(f"Result = {count}")
if __name__ == "__main__":
    main()