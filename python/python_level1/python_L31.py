def main():
    x = int(input("Enter Number: "))
    temp = (x // 100)  
    sec = (x//10)
    second = sec % 10       
    first=(x%10)    
    sum = temp + second + first
    y = 0
    if(sum >= 9):
        y = (sum // 10) + (sum % 10)
        if(y >= 9):
            y = (y // 10) + (y % 10)
    else:
        y = sum
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
