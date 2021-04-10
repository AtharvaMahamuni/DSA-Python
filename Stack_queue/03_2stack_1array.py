def pop1(a):
    # code here
    return(a.pop(0))


def pop2(a):
    # code here
    return(a.pop())


def push1(a, x):
    # code here
    a.insert(0, x)


def push2(a, x):
    # code here
    a.append(x)


arr = []

push1(arr, 10)
push1(arr, 20)

push2(arr, 30)
push1(arr, 40)

print(pop1(arr))
print(pop1(arr))
print(pop2(arr))
