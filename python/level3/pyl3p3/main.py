def sum14(no):
# Your Program Here
  a=int(no%10)#1's
  b=int(no/10)#first2
  c=int(b%10)#10's
  d=int(b/10)#100's
  sum_of_digits=int(a+c+d)
# Calculate the sum of digits and check if it equals 14
#  sum_of_digits = sum(int(digit) for digit in str(no))
  if sum_of_digits == 14:
    return 1
  else:
    return 0
def main():
  number = int(input("Enter a number: "))
  result = sum14(number)
  if result == 1:
    print("Sum of Digits is 14")
  else:
    print("Sum of Digits is not 14")
if __name__ == "__main__":main()