count = 0

for num in range(1000, 10000):
    s = str(num)
    
    if s[0] <= s[1] <= s[2] <= s[3]:
        count += 1

print(count)

