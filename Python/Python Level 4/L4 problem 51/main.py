#Python Level 4 | Problem 51 
x=input("Enter string:")
y=input("Enter character:")[0]
for i in range(0,len(x)-1):
    if(x[i]==y):
        print(i+1)
        