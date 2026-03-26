#Python Level 3 | Problem 1 
def function(no1):
# Define and initialize no2
    no2 = 0
    no2=no1+2
# Your Program Here 
    return no2
def main():
    number1 = int(input("Enter a number: "))
    number2 = function(number1)
    print(number2)
if __name__ == "__main__":
    main()