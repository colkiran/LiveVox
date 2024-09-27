
def my_decorator(func):
    # func = "say_hello"
    def wrapper():
        print("Something before the function.")
        func()  # Call the original function
        print("Something after the function.")

    return wrapper


@my_decorator           #say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()