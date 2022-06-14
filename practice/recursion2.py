def decToBin(n):
    if n == 1 or n == 0:
        return str(n)
    
    return (decToBin(n//2) + str(n%2))


print(decToBin(18))