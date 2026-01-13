"""
lambda arguments: expression
"""


squre = lambda x: x*x

print(squre(2))
"""
    Gap
"""
sumofnum = lambda a,b: a+b

print(sumofnum(2,3))

"""
    Gap
"""
number = [1,2,3,4,5]

squred = list(map(lambda x:x**x, number))

print(squred)

number_two = [1,2,3,4,5]

squre_two = list(map(lambda x:x**x, number))

print(squre_two)

