x =int(input("Enter Number: "))
   # Your Code Here
m=int(x/10)#first3
n=int(m/10)#first2
o=int(m%10)#10's
p=int(n%10)#100's
q=int(p+o)
if q>10:
  print("success")
else:
  print("fail")