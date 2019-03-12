def fibo(n):
    if n > 2:
        return fibo(n - 2) + fibo(n - 1)
    else:
        return 1
