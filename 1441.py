def count_calls(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"Function '{func.__name__}' was called {calls} ")
        return func(*args, **kwargs)

    return wrapper

@count_calls
def say_hello():
    print("Hello!")

say_hello()


def validate_inputs(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Invalid argument type: {arg}")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Incorrect argument value type {key}: {value}")
        return func(*args, **kwargs)

    return wrapper

@validate_inputs
def add(a, b):
    return a + b

print(add(10, 5))
print(add(10, "5"))


def add_affix(prefix="", suffix=""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}{result}{suffix}"
        return wrapper
    return decorator


@add_affix(prefix=">> ", suffix=" <<")
def greet(name):
    return f"Hello, {name}"

print(greet("Hanna"))
