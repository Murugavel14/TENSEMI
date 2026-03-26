def swapNumbers(no):
    temp = no
    swp = ((temp % 10) * 10) + (temp // 10)
    return swp
def main():
    number1 = int(input("Enter a number: "))
    print(swapNumbers(number1))
if __name__ == "__main__":
    main()
