x = int(input("Enter a number: "))
sum_of_digit = 0
while x > 0:
    digit = x%10
    sum_of_digit += digit
    x = x//10 
    
print (sum_of_digit)