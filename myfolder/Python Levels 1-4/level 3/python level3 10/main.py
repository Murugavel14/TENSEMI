def count_Digits(no):
    count = 0
    n = str(no)
    for i in range (0, len(n)):
        count += 1 
    return count 
def main():
    number1 = int(input("Enter a number: "))
    result = count_Digits(number1)
    print(result)
if __name__ == "__main__": main()