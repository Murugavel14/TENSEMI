def reverse_number(number):
    rev=0;
    while number>0:
      a=int(number%10)#1's
      rev=int(rev*10)+a
      number=int(number/10)
    return rev
def main():
 # number = 123  # Replace with your logic to get a 
  number = int(input("?"))
  result = reverse_number(number)
  print(f"The reversed number (assuming reverse_number works) would be: {result}")
if __name__ == "__main__":main()