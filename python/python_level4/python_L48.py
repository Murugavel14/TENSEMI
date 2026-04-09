def main():
    arr = [6, 12, 3, 15, 7]
    n = len(arr)
    result = [0] * n
    carry = 0
    for i in range(n - 1, -1, -1):
        temp = arr[i] + carry
        result[i] = temp % 10
        carry = temp // 10
    print(result)
if __name__ == "__main__":
    main()



