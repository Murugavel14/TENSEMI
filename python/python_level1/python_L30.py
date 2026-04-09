def main():
    x = int(input("Enter Number: "))
    first  = (x % 1000)		# (7595 % 1000)  595
    second = (first // 100)		# (595 // 100)   5
    ter = (first % 100)		# (595 % 100)   95
    three = (ter // 10)		# (95 // 10)    9
    if(three > second):
        if(7 < three):
            y = "Succss"
        else:
            y = "Failure"
    else:
        y = "Failure"
    print(three,second)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
