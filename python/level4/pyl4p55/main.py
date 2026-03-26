def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b
x=input("num1")
y=input("num2")
a=int(x)
b=int(y)
print("chooce operation")
print("1.addition")
print("2.subtraqction")
print("3.multiplication")
print("4.divition")
opt=input("choose 1,2,3,4")
if opt in('1','2','3','4'):
  if opt=='1':
    print("addition:",add(a,b))
  elif opt=='2':
    print("subtraction",sub(a,b))
  elif opt=='3':
    print("multipliction",mul(a,b))
  elif opt=='4':
    print("divition",div(a,b))
else:
  print("enter correct operation")