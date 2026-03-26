def int_arr(a,n):
 result=""
 for i in range(n):
  result=result+str(a[i])
 print("result",result)
  
n=int(input("enter size"))
a=[]
for i in range(n):
  x=int(input(f"val of {i}"))
  a.append(x)
print("int array",a)
int_arr(a,n)