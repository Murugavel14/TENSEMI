def function(no1,no2):
 if(no1==no2):
   return 1
 else:
   return 0
def main():
  n1 = int(input("Enter a number1: "))
  n2 = int(input("Enter a number2: "))
  same = function(n1,n2)
  if same:
    print("same")
  else:
    print("Not same")
if __name__ == "__main__":main()