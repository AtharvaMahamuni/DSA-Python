class Solution:
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self, a, n, b, m):

        # code here

        a = set(a)
        b = set(b)

        return len(a.union(b))


s = Solution()

a = list(map(int, input().split()))
b = list(map(int, input().split()))


print(s.doUnion(a, len(a), b, len(b)))
