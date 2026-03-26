num=input("num?")

first=int(num[0])      # first digit
rest=num[1:]           # remaining digits

if int(num)%2==0:
  a=num
else:
  if first%2!=0:
    first=first-1
    a=str(first)+rest
  else:
    a=num
print(a)