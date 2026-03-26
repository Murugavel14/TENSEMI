#Python Level 4 | Problem 48 
#def main():
"""    x=int(input("Enter the array size:"))
    arr=[]
    print("Enter the array elements:")
    for i in range(x):
        value=int(input(f"Enter value {i+1}:"))
        arr.append(value)
    print("Array is:",arr)
    result=[0]*(x+1)
    carry=0
    for i in range(len(arr)-1,-1,-1):
        total=arr[i]+carry
        result[i+1]=total%10
        carry=(total//10)
    result[0]=carry
    print(f"New array:{result}")
if __name__ == "__main__":
    main()   """

x=int(input("Enter the size of the array:"))
arr=[]
print("Enter the elements of the array:")
for i in range(x):
    value=int(input(f"Enter array element{i+1}:"))
    arr.append(value)
print("Array is:",arr)
#result=[0]*arr[i+1]
#carry=0
for i in range(len(arr)-1,-1,-1):
    if arr[i]>=10:
        carry=arr[i]//10
        arr[i]=arr[i]%10
        if i!=0:
            arr[i-1]+=carry
        else:
            arr.insert(0,carry)
print("New array :",arr)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        