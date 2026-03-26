x =int(input("Enter Number: "))
   # Your Code Here
m=int(x%10)#1's
n=int(x/10)#first2
o=int(n/10)#100's
p=int(m+o)
if p<10:
  print("success")
else:
  print("fail")