def subset(arr, index, holder=[]):
    if len(arr) == index:
        sol.append(holder)
        return

    subset(arr, index+1, holder+[arr[index]])
    subset(arr, index+1, holder)


array = [1, 2, 3]
sol = []
subset(array, 0)

print(sol)
