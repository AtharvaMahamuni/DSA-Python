
def merge(arr, low, mid, high):

    n1 = mid - low + 1
    n2 = high - mid

    left_arr = []
    right_arr = []

    for i in range(0, n1):
        left_arr.append(arr[low + i])

    for j in range(0, n2):
        right_arr.append(arr[mid + 1 + j])

    i = j = 0
    k = low

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1

        else:
            arr[k] = right_arr[j]
            j += 1

        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def divide(arr, low, high):

    if(low < high):

        mid = low + ((high - low)//2)  # Never miss floor division

        divide(arr, low, mid)
        divide(arr, mid+1, high)

        merge(arr, low, mid, high)


arr = list(map(int, input().split()))


high = len(arr) - 1

divide(arr, 0, high)

print(arr)
