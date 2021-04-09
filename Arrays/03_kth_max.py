

'''
# Kth max
# arr = set(map(int, input().split()))

# kth_max = int(input())

# arr = list(arr)

# arr.sort()

# # print(arr)
# print("Kth max : ", arr[len(arr)-kth_max])
'''

# Kth min

arr = set(map(int, input().split()))

kth_max = int(input())

arr = list(arr)

arr.sort()

# print(arr)
print("Kth max : ", arr[kth_max-1])
