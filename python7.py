def fib(n):
    def fib_n(curr, next, n):
        if(next > n):
            return curr
        else:
            return fib_n(curr * next, next + 1, n)
    return fib_n(1, 1, n)
    
print fib(100)