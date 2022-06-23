def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")

        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")

        return wrapped_f

    return wrap


class check():
    @decoratorFunctionWithArguments("hello", "world", 42)
    def sayHello(self, a1, a2, a3, a4):
        print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
check().sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")


# # --------------


def decorator(func):
    print("Inside decorator")

    def inner(*args, **kwargs):
        # code functionality here
        print("Inside inner function")
        print("I like")

        func(*args, **kwargs)
        return print("none")

    # returning inner function
    return inner


@decorator
def my_func():
    print("Inside actual function")
    return print("none my_func")


my_func()
# ---------------------------------


class decoratorWithoutArguments:

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")


@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("After first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("After second sayHello() call")


class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        # We can add some code
        # before function call

        self.function()

        # We can also add some code
        # after function call.


# adding class decorator to the function
@MyDecorator
def function():
    print("GeeksforGeeks")


function()
