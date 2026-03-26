def main():
    x = int(input("Enter Number: "))
    count = len(str(x))
    digit = (count -1)
    last  = (x // (10 ** digit))
    first = (x % 10)
    div   = (x %  (10 ** digit))
    first_rm = (div // 10) * 10
    result = (first * (10 ** (digit))) + first_rm + last
    print(f"Result = {result}") 
if __name__ == "__main__":
    main()



