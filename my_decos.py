import time

# define this behaviour first
def log(do_something):  # outer function: decorator

    def do_logging(a, b):  # nested decorating function
        print('now calculating with:', a, b)
        result = do_something(a, b)
        print('the result is', result)
        return result

    return do_logging


def timestamp(f):  # f is the function you want to decorate

    def print_timestamp(*args):
        print(time.asctime())  # do something additionally
        return f(*args) # call the decorated function

    return print_timestamp
