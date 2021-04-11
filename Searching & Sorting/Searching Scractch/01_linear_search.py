
arr = list(map(int, input().split()))

key = int(input())

isPresent = False

for i in arr:
    if i == key:
        isPresent = True
        break

if isPresent:
    print(1)

else:
    print(0)
