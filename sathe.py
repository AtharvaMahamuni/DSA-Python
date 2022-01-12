# for i in range(n):
#     store = i*i
#     if store > n:
#         return ((i-1)*(i-1))


# for i in range(nums):
#     jump = nums[i]

#     i = jump
#     jump = 0

#     if nums[i] == 0:
#         return False
#     return True


def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return total - sum_of_A

for i in nums:
    if nums.count(i) > 1:
        sorted(nums)
        miss = getMissingNo(nums)
        return (i+miss)