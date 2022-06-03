# resursive nth Fibonacci calculation script with memoization
# include type checking
# measure time of each function

import time

def memoize(f: callable) -> callable:
    """
    memoization decorator
    """
    cache: Dict[int, int] = {}
    def memoized_f(n: int) -> int:
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized_f

def time_it(f: callable) -> callable:
    """
    time decorator
    """
    def timed_f(n: int) -> int:
        start = time.time()
        result = f(n)
        end = time.time()
        print(f'{f.__name__}({n}) = {result} in {end-start:.2f} seconds')
        return result
    return timed_f

@time_it
@memoize
def fib_memo(n: int) -> int:
    """
    recursive fibonacci calculation with memoization
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_memo(n-1) + fib_memo(n-2)

def main(n):
    """
    main function
    """
    fib_memo(n)
    

if __name__ == "__main__":
    main(123) # 332 is themaximum recursion depth for this script