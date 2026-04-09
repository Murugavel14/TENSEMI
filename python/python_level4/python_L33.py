def check_assending(no):
    prev = 10   
    while no > 0:
        digit = no % 10
        if digit > prev:
            return False
        prev = digit
        no = no // 10
    return True
def main():
    count = 0
    for i in range(1000,9999):
        acsending = check_assending(i)
        if(acsending):
            count += 1
    print(count)
if __name__ == "__main__":
    main()
