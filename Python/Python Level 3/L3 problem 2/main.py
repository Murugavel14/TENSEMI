#Python Level 3 | Problem 2 
def function(no1):
    no2 = 0
    # Your Program Here
    no2=no1-5
    return no2
def main():
    number1 = int(input("Enter a number: "))
    number2 = function(number1)
    print(number2)
if __name__ == "__main__":
    main()