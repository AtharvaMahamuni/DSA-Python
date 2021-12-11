num = int(input())
count = 0

for i in range(num):

    s = input()

    s1 = ""
    s2 = ""

    stop = s[0]

    for i in s:
        if i == stop:
            s1+=i
        else:
            break
    
    stop = s[len(s)-1]

    for i in s[::-1]:
        if i == stop:
            s2+=i
        else:
            break

    if s == (s1+s2):
        count += 1

print(count)