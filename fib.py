def fibo(n):
    def fib(n):
        i, n1, n2 = 0, 1, 1
        while i < n:
            yield n1
            n1, n2 = n2, n1+n2
        i = i + 1
    return list(fib(n))       