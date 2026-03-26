def main():
    x = int(input("Enter Number: "))
    result = ((x//10) * 10) + 2
    #alternate method
    check = (x%10)
    if(check == 2):
        y = x
    else:
        y = result
    # -- alternate method end --
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
