#Python Level 3 | Problem 4 
def is_prime(number):
#"""Placeholder function for checking prime numbers (logic not implemented)"""
    count=0
    for i in range(1,number+1):
        if(number%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False
    #pass  # This line indicates the function body is empty
def main():
#"""Placeholder function for getting input and checking primeness (logic not implemented)"""
    number = int(input("Enter number:"))  # Example number (replace with your logic to get input)
    result = is_prime(number)
    if result:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
if __name__ == "__main__":
    main()