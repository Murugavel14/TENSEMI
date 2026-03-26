def main():
    x =int(input("Enter Number: "))
    if((x>=0) and (x<=127)):
        print("ascii",chr(x),".")
    else:
        print("enter valid ascii")
   # print(f"Result = {y}")
if __name__ == "__main__":main()