def MissingNumber(A, n):

    for i in range(n):
        if (A[i] <= 0 or A[i] > n):
            continue
        val = A[i]

        while (A[val - 1] != val):
            nextval = A[val - 1]
            A[val - 1] = val
            val = nextval
            if (val <= 0 or val > n):
                break
    for i in range(n):
        if (A[i] != i + 1):
            return i + 1

    return n + 1

if __name__ == "__main__":
    arr1 = [1,3,6,4,1,2]
    a_size = len(arr1)
    missing = MissingNumber(arr1, a_size)
    print("The samllest positive missing number is",missing)

