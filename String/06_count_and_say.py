def countAndSay(n: int) -> str:

    if (n == 1):
        return "1"
    if (n == 2):
        return "11"

    s = "11"
    for i in range(3, n + 1):
        s += '$'
        l = len(s)

        cnt = 1
        tmp = ""

        for j in range(1, l):

            if (s[j] != s[j - 1]):

                tmp += str(cnt + 0)

                tmp += s[j - 1]
                cnt = 1
            else:
                cnt += 1

        s = tmp
    return s


print(countAndSay(1))
print(countAndSay(2))
print(countAndSay(3))
print(countAndSay(4))
print(countAndSay(5))
print(countAndSay(6))
print(countAndSay(7))
