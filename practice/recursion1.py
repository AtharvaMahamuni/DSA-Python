

def fib(n, diary={1:0, 2:1}):
    if n in diary:
        return diary[n]

    diary[n] = fib(n-1) + fib(n-2)
    return diary[n]

print(fib(100))