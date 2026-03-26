def main():
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    if(num1 < num2):
        first = (num2 // 10)
        second = (num2 % 10)
    else:
        first = (num1 // 10)
        second = (num1 % 10)
# ---- ALTERNATE METHOD HERE ---
#* largest = max(num1, num2)

first = largest // 10
second = largest % 10
*#
# ---- XXXXX-------
    y = (first + second)
    print(f"Result = {y}")
if __name__ == "__main__":
    main()


