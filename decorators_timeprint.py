# using the decorators to print time 
from time import time
class Timer:

    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.function(*args, **kwargs)
        end_time = time()
        print("Execution took {} seconds".format(end_time-start_time))
        return result

# adding a decorator to the function
@Timer
def some_function(delay):
    from time import sleep

    # introducing some time delay to simulate a time taking action
    sleep(delay)

some_function(3)
