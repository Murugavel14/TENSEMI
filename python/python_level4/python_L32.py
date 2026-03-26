def main():
    def digit_sum(n):
        total = 0
        while n > 0:
            digit = n % 10      # last digit eduthukkum
            total += digit      # add pannum
            n = n // 10         # last digit remove pannum
        if(total == 14):
            return True
        
    def is_prime(n):
        if n <= 1:
            return False
        if n % 2 == 0:
            return False
    
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True  
    count = 0
    for i in range(11,1_000_000,2):
        add_14      = digit_sum(i)
        if (add_14):
            check_prime = is_prime(i)
            #print("14 -> ",i)
            if (check_prime):
                #print("prime -> ",i)
                count += 1
    print(count)
                
if __name__ == "__main__":
    main()
