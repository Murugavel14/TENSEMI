def main():
    x = int(input("Enter Number: "))
    z=x//10
    a=x%10
    add = a + z
    y = (add == 10 and "Success") or "Failure"
    print(f"Result = {y}")
if __name__ == "__main__":
    main()
