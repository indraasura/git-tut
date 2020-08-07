def fibonacci(limit):
    fib = []
    fib[0] = 0
    fib[1] = 1
    for i in range(limit):
        fib[i] = fib[i-1] + fib[i-2]
    print(fib)
    
fibonacci(500)