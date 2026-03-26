count = 0
for i in range (1,10):
    pcount = 0 
    for j in range (1, i):
        if(i%j == 0):
            pcount +=1 
            if (pcount == 2):
                count += 1 
print (count)