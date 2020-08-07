def fibonacci(limit):
    if limit <= 1:
        return limit
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(100)