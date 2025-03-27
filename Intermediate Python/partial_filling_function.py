from functools import partial

def multiplays(x, y):
    return x * y

fun = partial(multiplays, 2)

print(fun(10))
print(fun(12))
