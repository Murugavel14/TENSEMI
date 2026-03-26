def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for num in range(2, 1_000_000):
    if is_prime(num):
        temp = num
        total = 0
        while temp > 0:
            digit = temp % 10 
            total += digit
            temp //= 10
        if(total == 14):
            count += 1
            
print(count)