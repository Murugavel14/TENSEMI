x=int(input("Enter a number: "))
rev=0
while x!=0:
#for x in range(x,0,-1):
    y=int(x%10)
    rev=int(rev*10+y)
    x=int(x/10)   # Remove last digit
print(rev)