#Python Level 4 | Problem 47
n = int(input("Enter the size of the array n:"))# array 1 size
m = int(input("Enter the size of the array 2:"))# array 2 size
arr = [] #first array created
print("Enter the elements for array n")
for i in range(n): #getting array 1 value
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)
arr1=[] #second array created
print("Enter the elements for array m")
for i in range(m): #getting array 2 value
    value = int(input(f"Enter element {i+1}: "))
    arr1.append(value)
print("Array n is:", arr) #print array 1 value
print("Array m is:", arr1) #print array 2 value
y=max(len(arr),len(arr1)) #find max length of both arrays for adding purpose
arr=[0]*(y-len(arr))+arr #make array 1 and array 2 size are same it will add 0 in extra space
arr1=[0]*(y-len(arr1))+arr1 #make array 1 and array 2 size are same it will add 0 in extra space
print("Array n is:",arr) #after adding 0 print array 1
print("Array m is:",arr1) # after adding 0 print array 2
result=[0]*(y+1) #initially the next element (y+1) is 0
carry=0 #initially carry also 0
for i in range(y-1,-1,-1): #start from last element
    total=arr[i]+arr1[i]+carry #add both arrays
    result[i+1]=total%10 #sum
    carry=total//10 #carry
result[0]=carry#carry should placed in first place of array sum will be last(y+1)
print(result)#print array
