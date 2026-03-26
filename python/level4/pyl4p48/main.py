n = int(input("Enter a size of the array n: "))
arr = []
print("Enter the element of array n")
for i in range (n):
    value = int(input(f"Enter a element for {i+1} "))
    arr.append(value)
print("Array of n: " ,arr)
result = [0]*(n+1)
carry = 0
for j in range (n-1, -1, -1):
    total = arr[j]+carry
    result[j+1] = total%10
    carry = total//10
result[0] = carry
print("output: ", result)