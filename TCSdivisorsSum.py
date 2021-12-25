num1 = int(input())

num2 = int(input())


divisor1 = []
divisor2 = []


for i in range(1, num1/2+1):
    if num1%(i) == 0:
        divisor1.append(i+1)


for i in range(1, num2/2+1):
    if num2%(i) == 0:
        divisor2.append(i+1)

if(sum(divisor1) == num2 and sum(divisor2) == num1):
    print("Yes")
else:
    print("No")