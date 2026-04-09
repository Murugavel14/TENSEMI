def main():
    sum = 0
    for i in range(71,80,2):
            sum = sum + i
    print(f"Result = {sum}")
if __name__ == "__main__":
    main()LEVEL 2 | PROBLEM 11
def main():
    x = int(input("Enter Number: "))
    count = 0
    temp = x
    while (temp > 0):
        temp //= 10		#TEMP = TEMP // 10
        count += 1		#COUNT = COUNT + 1
    print(f"Result = {count}") 
    # ---- ALTERNATE ----
    count = len(str(x))
    # ---- xxxxx ---
if __name__ == "__main__":
    main()
