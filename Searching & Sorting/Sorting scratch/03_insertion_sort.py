
arr = list(map(int, input().split()))


for i in range(1, len(arr)):

    temp = arr[i]
    j = i - 1

    while j > -1 and temp < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = temp


print(arr)
