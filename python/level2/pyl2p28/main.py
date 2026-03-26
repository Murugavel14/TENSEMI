x=int(input("n1?"))
y=int(input("n2?"))
big=max(x,y)
while True:
  if big%x==0 and big%y==0:
    print(big)
    break
  big=big+1