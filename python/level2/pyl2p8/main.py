for x in range(11,100):
    if(x%2==0):
      a=int(x%10)#1's
      b=int(x/10)#10's
      if(a+b==6):
        print(x)