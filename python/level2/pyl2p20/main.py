pcount=0
for i in range(0,10):
  count=0
  for x in range(1,i+1):
    if(i%x==0):
      count=count+1
  if(count==2):
    pcount=pcount+1
print(pcount)