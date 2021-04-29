

string = input()

string = list(string)

setString = set(string)

for i in setString:

    count = 0

    for j in string:

        if i == j:
            count += 1

    if count > 1:
        print(i, " : ", count)
