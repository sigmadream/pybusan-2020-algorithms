import random
import sys
import os
from generic_search import linear_contains, binary_contains

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ProfilerTools.Perf import Perf


def exercise_1(maximum):
    ls = [random.randint(0, maximum) for _ in range(1_000_000)]

    @Perf(message="Linear Search")
    def call_linear_search():
        return linear_contains(ls, random.randint(0, maximum))

    @Perf(message="Binary Search")
    def call_binary_search():
        return binary_contains(ls, random.randint(0, maximum))

    print(">> List Unsorted")
    call_linear_search()
    call_binary_search()

    print(">> List Sorted")
    ls.sort()
    call_linear_search()
    call_binary_search()


if __name__ == "__main__":
    exercise_1(100)
