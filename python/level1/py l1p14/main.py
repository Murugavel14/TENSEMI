x = int(input("Enter Number: "))
   # Your Code Here
a=int(x%10)#last digit
b=int(x/10)#first two digit
c=int(b%10)#2 digit
d=int(b/10)#3digit
e=int(a*100)
f=int(c*10)
g=int(e+f+d)
#e=int((((a*100)+d)*10)+d)
#y=((x%10)*100)+(((x//10)%10)*10)+((x//10)//10)
print(f"Result = {g}")