def main():
    x = int(input("Enter Number: "))
    a=(x//100) % 100  #1ST
    z=x//10
    b=(z%10) * 10     #2ND
    c=(x%10) * 100    #3RD
    y=c+a+b
    print(f"Result = {y}")
if __name__ == "__main__":
    main()







