from functools import wraps
from dataclasses import dataclass
from typing import Any, Optional


NO_RETURN = object()


@dataclass
class Call:
    args: tuple
    kwargs: dict
    return_value: Any = NO_RETURN
    exception: Optional[BaseException] = None


def record_calls(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        wrapper_function.call_count += 1
        call = Call(args, kwargs)
        wrapper_function.calls.append(call)
        try:
            call.return_value = original_function(*args, **kwargs)
        except BaseException as e:
            call.exception = e
            raise
        return call.return_value

    wrapper_function.call_count = 0
    wrapper_function.calls = []
    return wrapper_function

# class record_calls(object):
#
#     def __init__(self, original_func):
#         self.original_func = original_func
#
#     def __call__(self, *args, **kwargs):
#         return self.original_func
