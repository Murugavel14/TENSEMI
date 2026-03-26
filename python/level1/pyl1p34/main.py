x1=int(input("n1?"))
x2=int(input("n2?"))
a = (x1 // 10) % 10 # 1o's of x1
b = (x2 // 10) % 10 # 10's of x2
if(a>b):
  c=x1
else:
  c=x2
d=int(c%10)#1's
e=int(c/100)#100's
print(d-e)