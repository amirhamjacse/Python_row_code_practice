"""
Function annotations add metadata to function parameters and return types but do not enforce types.
"""

def show_info(name: str, age: int) -> str:
    return f"name: {name}, age: {age}"

print(show_info("amir", 27))


def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))  # Output: 30
