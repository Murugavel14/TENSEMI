#Python Level 3 | Problem 5 
def find_number_of_zeros(number):
#"""Placeholder function for finding the number of zeros (logic not implemented)"""
    count=0
    while(number>0):
        rem=number%10 
        if(rem==0):
            count+=1 
        number//=10
    return count
#pass  # This line indicates the function body is empty
# Example usage (without input or logic):
number = int(input("Enter the number:"))  # Replace with your logic to get a number
result = find_number_of_zeros(number)
# Print result (but the result won't be meaningful without actual logic)
print(result)