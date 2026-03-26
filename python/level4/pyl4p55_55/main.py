def main():
    start = input()
    while (start == "calc" or start == "Calc"):
        data = input("Calc> ")
        if (data == "Exit" or data == "exit"):
            print("Exitingg.........")
            break
        else:
            try:
                if '+' in data:
                    parts = data.split('+')
                    num1 = int(parts[0])
                    num2 = int(parts[1])
                    print(num1 + num2)
                elif '-' in data:
                    parts = data.split('-')
                    num1 = int(parts[0])
                    num2 = int(parts[1])
                    print(num1 - num2)
                elif '*' in data:
                    parts = data.split('*')
                    num1 = int(parts[0])
                    num2 = int(parts[1])
                    print(num1 * num2)
                elif '/' in data:
                    parts = data.split('/')
                    num1 = int(parts[0])
                    num2 = int(parts[1])
                    print(num1 / num2)
                else:
                    print(f'"{data}" Is Not Allowd')
            except:
                print("Invalid")
    else:
        print(start, " Is Not Allowd")
if __name__ == "__main__":
    main()