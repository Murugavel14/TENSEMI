count = 0
for i in range(100, 1000):  
    pcount = 0 
    for j in range(1, i + 1):  
        if (i % j == 0):
            pcount += 1 
            
    if pcount == 2:  
        count += 1
        
print(count)