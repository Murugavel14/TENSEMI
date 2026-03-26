x=int(input("Enter a number: "))
sum=0
while x!=0:
#for x in range(x,0,-1):
    y=int(x%10)
    sum=sum+y
    x=int(x/10)   # Remove last digit
print(sum)