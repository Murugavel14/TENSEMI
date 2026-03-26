def is_prime(number):
    temp = number
    for i in range(2, number):
        if(temp % i == 0):
            return False
            break
    return True
        
def main():
    number = int(input("Enter Number: "))  
    result = is_prime(number)
    if result:
        print(f"{number} is a prime number.")
    else:       
        print(f"{number} is not a prime number.")
if __name__ == "__main__":
    main()
