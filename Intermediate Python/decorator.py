def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()  # Call the original function
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()


from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet():
    """This function says hello."""
    print("Hello, World!")

print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: This function says hello.
greet()


import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"{self.func.__name__} took {end - start:.4f} seconds")
        return result

@Timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()
