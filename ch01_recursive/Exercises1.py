import os
import sys
from functools import lru_cache
from math import log2, ceil

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ProfilerTools.Perf import Perf

def normal_fib(n):
    if n == 0:
        return n
    a = 0
    b = 1
    for _ in range(1, n):
        a, b = b, a + b
    return b

@lru_cache(maxsize=None)
def better_fib(index):
    if index == 0:
        return 0, 1
    else:
        a, b = better_fib(index // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if index % 2 == 0:
            return c, d
        else:
            return d, c + d


@Perf(message="Normal Fib", unit="us")
def call_normal_fib(index):
    return normal_fib(index)


@Perf(message="Better Fib", unit="us")
def call_better_fib(index):
    return better_fib(index)


if __name__ == "__main__":
    index = 100_000
    call_normal_fib(index)
    call_better_fib(index)
