def main():
    x = int(input("Enter Number: "))
    div = 0
    sum = 0
    temp = x
    while (temp > 0):
        div  = temp % 10
        temp //= 10
        sum = ((sum * 10) + div)
    print(f"Result = {sum}") 
if __name__ == "__main__":
    main()
