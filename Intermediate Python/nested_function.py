def outer():
    msg = "Hello hamja"

    def inner():
        print(msg)  # 'inner()' remembers 'msg' from 'outer()'
    
    return inner  # Returning function

closure_func = outer()
closure_func()  # Output: Hello hamja


def counter():
    count = 0
    def increment():
        nonlocal count # the count is from outer function that why used 'nonlocal'
        count += 1
        return count
    return increment

inc = counter()
print(inc())  # Output: 1
print(inc())  # Output: 2
print(inc())  # Output: 3
