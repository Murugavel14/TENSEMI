count = 0
for i in range (100000):
    n = i
    sum = 0 
    
    while (n > 0):
        sum += n%10 
        n = n//10
    
    if(sum == 14):
        count += 1
print(count)