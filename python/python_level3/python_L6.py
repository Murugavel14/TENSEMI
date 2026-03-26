def reverse_number(number):
    temp = str(number)
    return (temp[::-1])
    
def main():
    number = int(input("Enter Number: "))
    result = reverse_number(number)
    print(f"The reversed number (assuming reverse_number works) would be: {result}")
if __name__ == "__main__":
    main()

