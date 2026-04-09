def check_assending(no):
    temp = no
    length = len(str(no))
    count = 0
    forward = 0
    check = 0
    while temp > 0:
        div = temp % 10     #1234 --> 4   
        temp = temp // 10   #1234 --> 123 
        forward = temp % 10 #123 --> 3   
        if(temp > 10):
            check = (div - forward) #4 - 3 --> 1 
            print("div - forward",div,forward)
            if(check == 1):
                count += 1
                print("d,t,f,c",div, temp, forward, check)
        else:
            check = div - temp
            print("div - temp",div,temp)
            print("d,t,f,c",div, temp, forward, check)
            if(check == 1):
                count += 1
                print(div, temp, forward, check)
            elif(temp == 0):
                count += 1
                print("elif",div,temp,forward,check)
        print("count",count)
    if(length == count):
        return "YES"
    else:
        return "No"
def main():
    number1 = int(input("Enter a number: "))
    print("Result = ",check_assending(number1))
if __name__ == "__main__":
    main()
# ---- without print ----
def check_assending(no):
    temp = no
    length = len(str(no))
    count = 0
    forward = 0
    check = 0
    while temp > 0:
        div = temp % 10     #1234 --> 4   | 123 --> 3    | 12 --> 
        temp = temp // 10   #1234 --> 123 | 123 --> 12 | 12 --> 1 
        forward = temp % 10 #123 --> 3   | 12  --> 2
        if(temp > 10):
            check = (div - forward) #4 - 3 --> 1 | 3 - 2 --> 1
            if(check == 1):
                count += 1
        else:
            check = div - temp
            if(check == 1):
                count += 1
            elif(temp == 0):
                count += 1
    if(length == count):
        return "YES"
    else:
        return "No"
def main():
    number1 = int(input("Enter a number: "))
    print("Result = ",check_assending(number1))
if __name__ == "__main__":
    main()
#------- x x x x -----------

