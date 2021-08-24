def decimal_to_binary(val):

    if val <= 1:
        return str(val)

    else:
        return decimal_to_binary(val//2) + decimal_to_binary(val%2)



print(decimal_to_binary(11))
print(decimal_to_binary(1234))