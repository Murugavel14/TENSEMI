def main():
    x = int(input("Enter Number: "))
    temp = (x // 100)           #4 --> slipt (4,3)
    four = (temp % 10) * 1000   #3 --> take (3 x 1000) 
    three = (temp // 10) * 100  #2 --> take (4 x 100)
    last = (x % 100)            #1 -->(2,1)
    y= four + three + last      
    print(f"Result = {y}")
if __name__ == "__main__":
    main()






