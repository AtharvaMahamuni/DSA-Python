def findFibth(N, diary={1:0, 2: 1}):
    
    if N in diary:
        return diary[N]
    
    else:
        diary[N] = findFibth(N-1, diary) + findFibth(N-2, diary)
        return diary[N]


print(findFibth(7))
print(findFibth(13))
print(findFibth(1000))