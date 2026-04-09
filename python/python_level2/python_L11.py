def main():
    x = int(input("Enter Number: "))
    div = 0
    sum = 0
    temp = x
    while (temp > 0):
        div  = temp % 10	#(123456 % 10)  6 
        temp //= 10	#(123456 // 10)  100000
        sum = sum + div 	#(0 + 6 )  6
    print(f"Result = {sum}") 
if __name__ == "__main__":
    main()


