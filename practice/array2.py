
def findRotationPoint(arr):

    low = 0
    high = len(arr) - 1

    while (high >= low):

        mid = low + (high - low) // 2

        if(arr[mid] < arr[mid - 1]):
            return mid

        elif(arr[mid] > arr[mid + 1]):
            return (mid+1)

        elif(arr[mid] > arr[high]):
            low = mid + 1

        elif(arr[mid] < arr[low]):
            high = mid - 1


print(findRotationPoint([6, 7, 8, 9, 1, 2, 3, 4, 5]))
