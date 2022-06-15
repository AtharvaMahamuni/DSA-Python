def findSame(arr1, arr2, arr3):

    p1 = p2 = p3 = 0

    while(p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3)):

        if arr1[p1] == arr2[p2] and arr1[p1] == arr3[p3]:
            return arr1[p1]

        elif arr1[p1] <= arr2[p2] and arr1[p1] <= arr3[p3]:
            p1 += 1

        elif arr2[p2] <= arr1[p1] and arr2[p2] <= arr3[p3]:
            p2 += 1

        elif arr3[p3] <= arr1[p1] and arr3[p3] <= arr2[p2]:
            p3 += 1

    return "No same element found"


print(findSame([1, 2, 3, 4, 5, 6], [2, 4, 5, 6, 7], [1, 3, 4, 9]))
