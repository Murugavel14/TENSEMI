def main():
    x = int(input("Enter Number: "))
    first  = (x % 1000)		# (7595 % 1000)   595
    second = (first // 100)		# (595 // 100)   5
    ter = (first % 100)		# (595 % 100)   95
    three = (ter // 10)		# (95 // 10)   9
    y = ( three < second and “Failure” ) or “success”
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
