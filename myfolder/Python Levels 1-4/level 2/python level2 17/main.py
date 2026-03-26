num = int(input("Enter number: "))

if num <= 1:
    print("Not Prime and sum of digit is not 14")
else:
    for i in range(2, num):
        if num % i == 0:
            if ((num // 10)+(num % 10) == 14):
               print("Not Prime but sum of digit is 14")
            else: 
                print ("not prime and some digit is not 14")
            break
    else:
        if ((num//10)+(num%10)) == 14:
           print("Prime and some of digit is 14")
        else:
            print("prime but some of digit is not 14")