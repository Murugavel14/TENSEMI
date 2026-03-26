#Python Level 4 | Problem 47
n = int(input("Enter the size of the array n:"))
m = int(input("Enter the size of the array 2:"))
arr = []
print("Enter the elements for array n")
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)
arr1=[]
print("Enter the elements for array m")
for i in range(m):
    value = int(input(f"Enter element {i+1}: "))
    arr1.append(value)
print("Array n is:", arr)
print("Array m is:", arr1)
y=max(len(arr),len(arr1))
arr=[0]*(y-len(arr))+arr
arr1=[0]*(y-len(arr1))+arr1
print("Array n is:",arr)
print("Array m is:",arr1)
result=[0]*(y+1)
carry=0
for i in range(y-1,-1,-1):
    total=arr[i]+arr1[i]+carry
    result[i+1]=total%10
    carry=total//10
result[0]=carry
print(result)