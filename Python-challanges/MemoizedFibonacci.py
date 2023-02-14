# Problem Context
# The Fibonacci sequence is traditionally used to explain tree recursion.
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

