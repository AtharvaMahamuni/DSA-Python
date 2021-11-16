
array_1 = list(map(int, input().split(" ")))
array_2 = list(map(int, input().split(" ")))


array_new = list(set(array_1)) + list(set(array_2))

array_new.sort()

ans = 0 

if len(array_new)%2 == 0:
    ans = array_new[len(array_new)//2]

else:
    ans = (array_new[len(array_new)//2]+array_new[len(array_new)//2+1])//2

print(ans)