def fib():
    d = {}
    d[0] = 0
    d[1] = 1
    yield d[0]
    k = 1
    while k >= 0:
        yield d[k]
        d[k+1] = d[k] + d[k-1]
        k += 1


print(fib())


