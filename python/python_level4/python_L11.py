def main():
    x = int(input("Enter Number: "))
    temp = x
    sum = 0
    while temp > 0:
        div = temp % 10
        temp //= 10
        sum += div
    print(f"Result = {sum}")
if __name__ == "__main__":
    main()
