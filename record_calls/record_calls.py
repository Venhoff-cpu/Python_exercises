from functools import wraps


def record_calls(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        wrapper_function.call_count += 1
        return original_function(*args, **kwargs)

    wrapper_function.call_count = 0

    return wrapper_function

# class record_calls(object):
#
#     def __init__(self, original_func):
#         self.original_func = original_func
#
#     def __call__(self, *args, **kwargs):
#         return self.original_func
