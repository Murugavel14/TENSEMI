total = 0
for i in range (10000, 1000, -1):
    pcount = 0
    for j in range (1,i+1):
        if(i%j == 0):
            pcount += 1
    if(pcount == 2):
        total += i
        break
print(total)