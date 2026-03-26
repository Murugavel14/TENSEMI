n1 = int(input("n1? "))
n2 = int(input("n2? "))

a = (n1 // 100) + (n1 % 10)   # 100's + 1's of n1
b = (n2 // 100) + (n2 % 10)   # 100's + 1's of n2

if(a > b):
    c = n1
else:
    c = n2

d = c // 100          # 100's digit
e = (c // 10) % 10    # 10's digit
f = c % 10            # 1's digit

print(d + e + f)