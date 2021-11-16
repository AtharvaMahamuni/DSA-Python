
n = int(input())

m = int(input())


divisible_by = 0

not_divisible_by = 0


for i in range(1, m+1):

    if(i%n == 0):
        divisible_by += i

    else:
        not_divisible_by += i

print(not_divisible_by-divisible_by)