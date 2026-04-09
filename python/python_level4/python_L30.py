def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def main():
    for i in range(99999999, 9999999, -1):
        if is_prime(i):
            print(i)
            break
if __name__ == "__main__":
    main()
