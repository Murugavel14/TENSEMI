num=int(input("?"))
count=0
for i in range(1,num+1):
  if(num%i==0):
    count=count+1 
if(count==2):
 
  a=int(num%10)#1's
  b=int(num/10)#10's
  c=int(a+b)
  if(c==14):
    print("prime & sum of digit is equal to 14")
  else:
    print("prime,but sum of digit is not equal to 14")
else:
  a=int(num%10)#1's
  b=int(num/10)#10's
  c=int(a+b)
  if(c==14):
    print("not prime but sum of digit is equal to 14")
  #else:
   # print("not equal to 14")