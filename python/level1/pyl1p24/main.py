x = int(input("Enter Number: "))
   # Your Code Here
m=int(x%10)#1's
n=int(x/10)#first2
o=int(n/10)#100's
p=int(x-(5*(m==o)))
print(p)
    #if m==p:
 # print("success")
#else:
#  print("fail")