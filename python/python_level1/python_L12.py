def main():
    x = int(input("Enter Number: "))
    a=x//100
    z=x//10
    b=z%10
    c=x%10
    y=c+a+b
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
