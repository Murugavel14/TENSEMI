def main():
    def palindrome(no):
        num = str(no)
        pali_num = num[::-1]
        if(num == pali_num):
            return True
    
    count = 0
    for i in range(1, 100_000):
        result = palindrome(i)
        if(result):
            count += 1;
    print(count)
if __name__ == "__main__":
    main()
