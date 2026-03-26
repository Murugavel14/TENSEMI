def sum14(no):
    temp = no
    sum_of_digits = 0
    while temp > 0:
        div = temp % 10
        temp = temp // 10
        sum_of_digits = sum_of_digits + div
    if sum_of_digits == 14:
        return 1
    else:
        return 0
def main():
    number = int(input("Enter a number: "))
    result = sum14(number)
    if result == 1:
        print("Sum of Digits is 14")
    else:
        print("Sum of Digits is not 14")
if __name__ == "__main__":
        main()
