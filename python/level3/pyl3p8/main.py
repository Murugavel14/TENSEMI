def check_ascending(no):
  for i in range(0,len(no)-1):
    if no[i] > no[i+1]:
      return 0
  return 1

def main():
  number = input("Enter a number: ")
  ass = check_ascending(number)
  if ass:
    print("Yes")
  else:
    print("No")
if __name__ == "__main__":main()