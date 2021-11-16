
def isPrime(number):
    
    for i in range(number//2 + 1):
        if number%i == 0:
            return False
        else:
            return True

num = int(input())
ans_arr = []

list_nu = []

for i in range(num):
    list_nu.append(int(input()))


for i in list_nu:

    if isPrime(i):
        ans_arr.append("Prime\n")
    else:
        ans_arr.append("Composite\n")


print(ans_arr)