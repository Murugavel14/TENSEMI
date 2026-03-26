count = 0
for i in range (0, 1001):
    j = str(i)
    for k in range (0, len(j)):
        if(j[k] == '0'):
           count += 1
print(count)