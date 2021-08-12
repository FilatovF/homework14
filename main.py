"""Task 1"""

def logger(func):
    def deco_print(*args, **kwargs):
        return (f"Work with {func.__name__} function and with arguments {*args, *kwargs}")
    return deco_print



@logger
def add(x, y):
    return x + y



@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(4,5))
print(square_all(4,5))

"""Task2"""
from functools import wraps


def stop_words(words: list):
    def stop_word_search(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            a = func(*args, **kwargs)
            for word in words:
                if word in a:
                    a = a.replace(word, "*")
            return a
        return wrap

    return stop_word_search


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


"""Task3"""
def arg_rules(type_: type, max_length: int, contains: list):
    def validator(func):
        #@wraps(func)
        def wrap(*args, **kwargs):
            if not type(*args, **kwargs) == type_:
                print(f"The type of slogan must be {type_} - given {type(*args, **kwargs)}")
                return False
            if not max_length >= len(*args, **kwargs):
                print(f"The length of the input must be {max_length} max - given {len(*args, **kwargs)}")
                return False
            for i in contains:
                if not i in str(*args, **kwargs):
                    print(f"The name must contain {contains} - given {str(*args, **kwargs)} ")
                    return False
            return func(*args, **kwargs)
        return wrap
    return validator

@arg_rules(type_= str, max_length = 15, contains = ['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

