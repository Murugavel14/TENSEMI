def find_number_of_zeros(number):
    count = 0
    while (number >0):
        digit = int(number % 10) 
        if (digit == 0):
            count += 1
        number = int(number // 10)
    return count
number = int(input("Enter the Number: "))
result = find_number_of_zeros(number)
print(result)