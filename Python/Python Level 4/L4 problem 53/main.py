#Python Level 4 | Problem 53
a=input("Enter the string:")
count=0
for i in range(0,len(a)):
    if(a[i]==' '):
        count+=1 
print(count+1)