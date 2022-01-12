def prime(myNum):

    for i in range(1, myNum//2-1):
        if myNum%i == 0:
            return false
    return true

def divide(myNum):

    divide(myNum-1)
    divide(myNum+1)
    
    if prime(myNum):
        return myNum


num = int(input())

print(divide(num))  