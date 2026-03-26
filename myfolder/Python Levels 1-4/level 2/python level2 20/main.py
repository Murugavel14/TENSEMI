count = 0
for i in range (1, 10):
    c = 0
    for x in range (1, i+1):
        if (i%x) == 0:
            c = c + 1
    if(c == 2):
        count = count + 1
print (count)
