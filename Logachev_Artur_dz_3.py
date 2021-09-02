from functools import wraps
def typping(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=',')
        return func(*args)
    return wrapper

@typping
def calc_cube(*args):
    """this shows only with 'from functools import wraps'"""
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)