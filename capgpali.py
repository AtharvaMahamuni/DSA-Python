num = int(input())

my_sum = 0

while num != 0:
    my_sum = my_sum + num%10
    num //= 10

ans = 0
num = str(num)

if num == reversed(num):
    ans = 1

print(ans)