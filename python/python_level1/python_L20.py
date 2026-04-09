def main():
    x = int(input("Enter Number: "))
    ten = (x//100) * 100  #(695 // 100)  6 * 100  600 
    first = (x % 10)            #(695 % 10)     5
    y = ten + first              #600 + 5           605
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
