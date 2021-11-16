import math

cost = int(input())

year = int(input())

deprication_rate = int(input())

new_value = cost

if deprication_rate < 5 or deprication_rate > 100 or deprication_rate % 5 != 0:
    print("Invalid input")

else:
    for i in range(year-1):

        new_value = new_value * (100-deprication_rate) / 100

print(math.ceil(new_value))
