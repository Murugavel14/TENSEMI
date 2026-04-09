x = int(input("Enter a number: "))
a = x%100
p = a//10 
q = a%10
b = x//100
r = b//10 
s = b%10

y = p+q+r+s
print(y)