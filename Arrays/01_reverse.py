
def reverseArray(A, start, end):

    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


arr = list(map(int, input().split()))

print(arr)

reverseArray(arr, 0, len(arr)-1)

print(arr)
