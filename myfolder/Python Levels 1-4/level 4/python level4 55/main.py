start = input()
while(start == "Calc" or start == "calc"):
    data = input("calc>  ")
    if (data == "exit" or data == "Exit"):
        print ("Exit")
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
            elif '%' in data:
                parts = data.split('%')
                num1 = int(parts[0])
                num2 = int(parts[1])
                print(num1 % num2)
            else:
                print("Data is not allowded")
        except:
            print ("INVALID")
else: 
    print(f"data is not valid", {data})