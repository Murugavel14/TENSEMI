def check_assending(no):
    prev = 10   
    while no > 0:
        digit = no % 10
        if digit > prev:
            return "No"
        prev = digit
        no = no // 10
    return "Yes"
def main():
    number1 = int(input("Enter a number: "))
    print("Result = ",check_assending(number1))
if __name__ == "__main__":
    main()


