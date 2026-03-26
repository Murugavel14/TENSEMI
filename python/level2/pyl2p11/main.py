x=int(input("Enter a number: "))

count = 0

while x!=0:
#for x in range(x,0,-1):
    x=int(x/10)   # Remove last digit
    count=count+1

print("Output:", count)