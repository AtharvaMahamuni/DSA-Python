# word = input().split()

# for i in range(len(word)):
#     if word[i] == 'a':
#         word[i] = 'i'
#     elif word[i] == 'A':
#         word[i] = 'I'
#     elif word[i] == 'e':
#         word[i] = 'i'
#     elif word[i] == 'E':
#         word[i] = 'I'
#     elif word[i] == 'i':
#         word[i] = 'o'
#     elif word[i] == 'I':
#         word[i] = 'O'
#     elif word[i] == 'o':
#         word[i] = 'u'
#     elif word[i] == 'O':
#         word[i] = 'U'
#     elif word[i] == 'u':
#         word[i] = 'a'
#     elif word[i] == 'U':
#         word[ibaetriUto] = 'A'

# print(''.join(word))


num = int(input())
multiple1 = int(input())
multiple2 = int(input())

sum = 0

for i in range(1, num+1):
    # print(i, end=' ')
    if ((i % multiple1) == 0) or ((i % multiple2) == 0):
        sum += i
        print(i, end=' ')

print(sum)