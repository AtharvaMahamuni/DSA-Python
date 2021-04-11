arr = list(map(int, input().split()))

key = int(input())

isPresent = False

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high)//2

    if arr[mid] == key:
        isPresent = True
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1


if isPresent:
    print(1)

else:
    print(0)
