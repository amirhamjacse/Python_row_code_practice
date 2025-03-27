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
