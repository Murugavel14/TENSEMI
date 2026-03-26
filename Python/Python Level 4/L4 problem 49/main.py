#Python Level 4 | Problem 49
def main():
    x = int(input("Enter the array size: "))
    arr=[]
    print("Enter the array elements:")
    for i in range(x):
        value=int(input(f"Enter the array element{i+1}:"))
        arr.append(value)
    print(f"array is = {arr}")
    new_arr=''.join(str(i) for i in arr)
    print(new_arr)
if __name__ == "__main__":
    main()