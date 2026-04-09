def main():
    try:
        x = int(input("Enter Number: "))
    except ValueError:
        print("Not a valid Number")
    else:
        print("Valid Number")
if __name__ == "__main__":
    main()
