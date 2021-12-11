def maxDays(countTown):
    answer = 0
    maximum = max(countTown)
    total = sum(countTown)

    s = total - maximum


    if (s+1) < maximum:
        answer = (2*s)+1
    
    else:
        answer = total
    
    return answer