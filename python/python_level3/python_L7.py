def function(no1,no2):
    if(no1 == no2):
        return "SAME"
    else:
        return "NOT SAME"
def main():
    number1 = int(input("Enter a number1: "))
    number2 = int(input("Enter a number2: "))
    print("RESULT = ",function(number1, number2))
if __name__ == "__main__":
    main()
