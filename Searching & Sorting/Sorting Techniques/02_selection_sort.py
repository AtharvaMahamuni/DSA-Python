
arr = list(map(int, input().split()))

for i in range(len(arr)):
    mi = i
    for j in range(i, len(arr)):

        if arr[j] < arr[mi]:
            mi = j

    arr[i], arr[mi] = arr[mi], arr[i]


print(arr)
