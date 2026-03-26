x = int(input("Enter a number: "))
p = x%10
q = x//10
r = q%10
s = q//10
t = s%10
u = s//10

y = ((p*1000)+(r*100)+(t*10)+u)
print(y)