def main():
    x = int(input("Enter Number: "))
    temp = (x // 100) * 100 #ROUND OF 1200
    sec = (x//10)
    second = sec % 10       #2ND DIGIT INTO 1ST DIGIT
    first=(x%10) * 10       #1ST DIGIT INTO 2ND DIGIT
    y= temp + second + first
    print(f"Result = {y}")
if __name__ == "__main__":
    main()

