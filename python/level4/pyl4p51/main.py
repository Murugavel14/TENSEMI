def main():
   x = input("Enter string: ")
   y = input("char?")
   # Your Code Here
   z=len(x)
   for i in range(0,z):
    if(x[i]==y):
      print(i)
    #print(f"Result = {y}")
if __name__ == "__main__":main()