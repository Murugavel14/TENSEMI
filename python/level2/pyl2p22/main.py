x=int(input("Enter a number: "))
count=0
while x>9:
    
#for x in range(x,0,-1):
    y=int(x%100)
    if(y%2!=0):
      count=count+1
    x=int(x/10)   # Remove last digit
print(count)