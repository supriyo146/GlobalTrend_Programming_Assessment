# Write a Python decorator that measures the execution time of a function and logs it. Apply this decorator to a function that performs a computationally expensive task.




import time
import logging

logging.basicConfig(level=logging.INFO)

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@time_it
def expensive_function(n):
    sum = 0
    for i in range(n):
        sum += i ** 2
    return sum

expensive_function(100000)
