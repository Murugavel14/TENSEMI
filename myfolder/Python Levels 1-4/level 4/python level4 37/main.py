x = int(input("Enter a number: "))
if 0 <= x <= 127:
    print ("value : ", chr(x))
else:
    print("Enter a valid ASCII value")
