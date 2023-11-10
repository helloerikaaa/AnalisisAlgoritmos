def fibonacci_iterativo(n):
    fib = [0, 1]
    if n <= 1:
        return fib[n]
    else:
        for i in range(2, n + 1):
            fib.append(fib[i - 2] + fib[i - 1])
        return fib[n]
