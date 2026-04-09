def reverse_number(number):
 rev = 0
 while (number > 0):
    a = number % 10
    rev = (rev*10) + a 
    number = number// 10
 return rev
 
def main():
 number = int(input("Enter the Number: "))
 result = reverse_number(number)
 print(f"The reversed number (assuming reverse_number works) would be: {result}")
if __name__ == "__main__": main()