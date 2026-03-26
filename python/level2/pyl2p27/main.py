count=0
for i in range(0,100000+1):
  a=int(i%10)#1's
  b=int(i/10)#first 5
  c=int(b%10)#10's
  d=int(b/10)#first 4
  e=int(d%10)#100's
  f=int(d/10)#first 3
  g=int(f%10)#1000's
  h=int(f/10)#first 2
  i=int(h%10)#10000's
  j=int(h/10)#100000's
  k=int(a+c+e+g+i+j)
  if(k==14):
    count=count+1;
print(count)