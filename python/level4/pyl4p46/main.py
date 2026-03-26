def main():
    x = input("Enter Number: ")
   # Your Code Here
    arr=[]
    for i in range(len(x)):
      arr.append(int(x[i]))
    print(f"Result = {arr}")
if __name__ == "__main__":main()