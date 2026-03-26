def main():
    x = int(input("Enter Number: "))
    first  = (x % 1000)		# (7595 % 1000)   595
    second = (first // 100)		# (595 // 100)   5
    ter = (first % 100)		# (595 % 100)   95
    three = (ter // 10)		# (95 // 10)   9
    result = (second != three and x) or x – 5   #( result = second == three? x – 5 : x)
    y = result
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
