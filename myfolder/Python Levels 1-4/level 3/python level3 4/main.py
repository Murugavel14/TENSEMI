def is_prime(number):
 count = 0 
 for i in range (1, number + 1) :
    if (number % i == 0):
        count += 1 
 if (count == 2):
    return 1;
 else:
    return 0;
def main():
 
 number = int(input("enter the number: "))
 result = is_prime(number)
 if result:
    print(f"{number} is a prime number: ")
 else:
    print(f"{number} is not a prime number: ")
if __name__ == "__main__": main()