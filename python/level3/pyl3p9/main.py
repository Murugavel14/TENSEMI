def swapNumbers(no):
# Your Program Here
  m=int(no%10)#1
  n=int(no/10)#10
  o=int((m*10)+n)
  return o
#return anyNumber_Here
def main():
  n = int(input("Enter a number: "))
  x=swapNumbers(n)
  print(x)
if __name__ == "__main__":main()