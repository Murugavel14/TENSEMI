x=int(input("n1?"))
y=int(input("n2?"))
a=int(x%10)#1's of x
b=int(x/10)#10's of x
c=int(a+b)
d=int(y%10)#1's of y
e=int(y/10)#10's of y
f=int(d+e)
if(c>f):
  print(c)
else:
  print(f)