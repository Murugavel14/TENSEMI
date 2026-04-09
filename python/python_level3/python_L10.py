def count_Digits(no) :
    temp = no
    count = 0
    div = 0
    while temp > 0:
        div  = temp % 10
        temp = temp // 10
        count += 1
    return count
def main():
    number1 = int(input("Enter a number: "))
    print("Result = ",count_Digits(number1))
if __name__ == "__main__":
    main()
