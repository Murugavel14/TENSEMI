def main():
    x = int(input("Enter Number: "))
    first = (x // 10)             #(21 // 10)     2
    even  = (first % 2)        #(2 % 2)   0
    result = (even ==  1 and x) or x – 5  #(result = even? x : x - 5  
    y = result
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
