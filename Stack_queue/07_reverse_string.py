
def reverse(string):

    stack = []

    for char in string:
        stack.append(char)

    string = ""

    while stack:
        string = string + stack.pop()

    return string

string = input()

print(reverse(string))
