import functools
@functools.lru_cache()
def fibonacci(n):
    if n < 4:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
res = fibonacci(10)
print(res)
