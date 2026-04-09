def main():
    x = int(input("Enter Number: "))
    in1 = x // 100
    in2_ter = x // 10
    in2  = in2_ter % 10
    in3 = x % 10
    add = in1 + in2 + in3
    y = (add == 10 and "Success") or "Failure"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
