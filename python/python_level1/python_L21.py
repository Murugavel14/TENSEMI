def main():
    x = int(input("Enter Number: "))
    check = (x%10)
    even  = (check % 2)
    y = (even == 0 and x) or x – 5
    #alternate method
    y = x – 5 * (x % 2)
    # -- alternate method end --
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
