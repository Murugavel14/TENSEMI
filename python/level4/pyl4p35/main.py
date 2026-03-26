def main():
    x1 = int(input("Enter Number1: "))
    x2= int(input("Enter Number2: "))
    big=max(x1,x2)
    while True:
        if(big%x1==0 and big%x2==0):
          print(big)
          break
        big=big+1
    #print(f"Result = {y}")
if __name__ == "__main__":main()