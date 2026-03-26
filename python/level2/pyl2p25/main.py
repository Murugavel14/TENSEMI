x=int(input("Enter a number: "))
pcount=0
while x>0:
  count=0
  y=int(x%10)
  for i in range(1,y+1):
    if(y%i==0):
      count=count+1
  if(count==2):
    pcount=pcount+1
  x=int(x/10)
print(pcount)