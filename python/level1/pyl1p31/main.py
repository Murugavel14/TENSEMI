x=int(input("?"))
a=int(x%10)#1's
b=int(x/10)#first2
c=int(b%10)#10's
d=int(b/10)#100's
e=int(a+c+d)
if(e<10):
  print(e)
else:
  f=int(e%10)#1's of e
  g=int(e/10)#10's of e
  h=int(f+g)
  if(h<10):
    print(h)
  else:
    g=int(h%10)#1's of h
    i=int(h/10)#10's of h
    j=int(g+i)
    print(j)