def count_Digits(no):
# Your Program Here
  a=str(no)
  count=0
  for i in range(0,len(a)):
    count=count+1;
  return count
def main():
  number1 = int(input("Enter a number: "))
  x=count_Digits(number1)
  print(x)
if __name__ == "__main__":main()