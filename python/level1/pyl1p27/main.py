x = int(input("Enter Number: "))
   # Your Code Here
m=int(x%10)#1's
n=int(x/10)#first2
o=int(n%10)#10's
p=int(n/10)#100's
y=int(m+p+o)
if y==10:
  print("success")
else:
  print("fail")