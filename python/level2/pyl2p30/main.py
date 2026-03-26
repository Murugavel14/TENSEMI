x=int(input("n1?"))
y=int(input("n2?"))
small=min(x,y)
while True:
  if x%small==0 and y%small==0:
    print(small)
    break
  small=small-1