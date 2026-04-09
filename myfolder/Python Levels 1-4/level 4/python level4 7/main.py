x = int(input("Enter a number: "))
p = x%10
v = x//10
q = v%10
r = v//10

y = (p *100) + (q *10) + r
print(y)