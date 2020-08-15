from time import perf_counter_ns


class Perf(object):
    def __init__(self, unit="ms", message=None, trials=100):
        self.unit = unit
        self.message = message
        self.trials = trials

    def __call__(self, f):
        def wrapper_timer(*args, **kwargs):
            average = 1
            for _ in range(self.trials):
                before = perf_counter_ns()
                rv = f(*args, **kwargs)
                after = perf_counter_ns()
                average = (average + (after - before)) / 2
            conversion = self.convert_time()
            time = average / conversion
            print(f"Time Elapsed: {time:.3f} {self.unit}")
            if self.message is not None:
                print("f{self.message}")
            return rv

        return wrapper_timer

    def convert_time(self):
        if self.unit == "ns":
            conversion = pow(10, 0)
        elif self.unit == "us":
            conversion = pow(10, 3)
        elif self.unit == "ms":
            conversion = pow(10, 6)
        elif self.unit == "s":
            conversion = pow(10, 9)
        elif self.unit == "min":
            conversion = 6 * pow(10, 10)
        else:
            print(
                f"Bad unit given to @Perf, Valid units are: \n ns, us, ms, s, min \n Using default ms"
            )
            conversion = pow(10, 6)
            self.unit = "ms"
        return conversion
