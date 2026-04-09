def main():
    x = int(input("Enter Number: "))
    check = (x%100)          #(1234556 % 100)  56
    first = (check // 10)    #(56 // 10)   5 
    even  = (first % 2)      #(5 % 2) 1
    result = (even == 0 and x) or x - 5 #( result = even? x – 5 : x)
    y = result
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
