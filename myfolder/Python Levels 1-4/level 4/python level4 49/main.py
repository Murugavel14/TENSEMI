def convert_and_print(int_array):

    # "" -Join them together 
    char_string = "".join(str(i) for i in int_array) # Convert each integer to a string character
    
    print(f"result: {char_string}")

arr = [1, 4, 5, 8,5,4,3,3]

print("Array ", *arr) 
convert_and_print(arr)