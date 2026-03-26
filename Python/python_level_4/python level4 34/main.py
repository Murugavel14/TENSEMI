def is_palindrome(n):
    num = n
    rev = 0

    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10

    return num == rev


count = 0

for num in range(1, 100000):
    if is_palindrome(num):
        count += 1
        print (num)
print("Total palindrome numbers:", count)