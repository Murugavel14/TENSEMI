def find_number_of_zeros(number):
    temp = number
    count = 0
    while temp > 0:
        div = temp % 10
        temp = temp // 10
        if(div == 0):
            count += 1
    return count
number = int(input("Enter Number: "))
result = find_number_of_zeros(number)
print(result)
