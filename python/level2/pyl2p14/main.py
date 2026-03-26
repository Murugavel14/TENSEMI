num=input("num?")
if len(num)>1:
  a=num[-1]+num[1:-1]+num[0]
else:
  a=num
print(a)