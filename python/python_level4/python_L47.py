def add_arrays(A, B):
    i = len(A) - 1
    j = len(B) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        a = A[i] if i >= 0 else 0
        b = B[j] if j >= 0 else 0
        total = a + b + carry
        result.append(total % 10)
        carry = total // 10
        i -= 1
        j -= 1
    result.reverse()
    return result
print(add_arrays([9,9,9], [1]))
