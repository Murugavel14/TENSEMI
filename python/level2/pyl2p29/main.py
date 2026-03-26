x=int(input("n1?"))
y=int(input("n2?"))
z=int(input("n3?"))
big=max(x,y,z)
while True:
  if big%x==0 and big%y==0 and big%z==0:
    print(big)
    break
  big=big+1