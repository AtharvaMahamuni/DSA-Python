
arr = list(map(int, input().split()))

'''
O(n^2) time complexity
# arr.sort()

# max = arr[len(arr)-1]
# min = arr[0]
'''

max = arr[0]
min = arr[0]

for i in arr:
    if(max < i):
        max = i
    if(min > i):
        min = i

print("max: ", max)
print("min: ", min)
