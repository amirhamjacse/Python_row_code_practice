def show_parameter(*args, **kwargs):
    print(args)
    print(f"kwargs, {kwargs}")

show_parameter(1,2,3, name="amir")


def show_parameter(*args, **kwargs):
    print(args)
    print(f"kwargs, {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_parameter(1,2,3, name="amir")


def show_details(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Other Info: {args}")  # Tuple
    print(f"Additional Info: {kwargs}")  # Dictionary

show_details("Amir", "Python Developer", 25, city="Dhaka", country="Bangladesh")
