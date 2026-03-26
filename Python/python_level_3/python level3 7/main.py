def function(no1,no2):
 if (no1 == no2):
    return 1;
 else:
     return 0;
def main():
 number1 = int(input("Enter a number: "))
 number2 = int(input("Enter a number: "))
 x = function(number1, number2)
 if (x):
    number2 = "same"
 else:
     number2 = "not same"
 print(number2)
if __name__ == "__main__": main()