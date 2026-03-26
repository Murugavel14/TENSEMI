def check_assending(no):
    x = str(no)
    for i in range (0, len(x)-1):
        if x[i] > x[i+1]:
           return "no"
    return "yes"

def main():
    number1 = int(input("Enter a number: "))
    result = check_assending(number1)
    print(result)
if __name__ == "__main__": main()