def swapNumbers(no):
    n = no
    a = n % 10
    b = n // 10
    result = (a*10)+b
    return result
def main():
    number1 = int(input("Enter a number: "))
    result = swapNumbers(number1)
    print(result)
if __name__ == "__main__":
 main()