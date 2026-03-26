total = 0
for i in range (10, 100):
    pcount = 0
    for j in range (1,i+1):
        if(i%j == 0):
            pcount += 1
    if(pcount == 2):
        total += i
print(total)