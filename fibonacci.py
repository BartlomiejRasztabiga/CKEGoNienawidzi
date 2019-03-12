def fibo(n):
    if n > 2:
        return fibo(n - 2) + fibo(n - 1)
    else:
        return 1


print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
print(fibo(8))
print(fibo(9))
