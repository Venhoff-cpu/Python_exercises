# from contextlib import ContextDecorator
#
#
# class suppress(ContextDecorator):
#     def __init__(self, *exc_types):
#         self.exc_types = exc_types
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exception, traceback):
#         self.exception = exception
#         self.traceback = traceback
#         if isinstance(exception, self.exc_types):
#             return True
#
#         return False


# class suppress():
# '''Class based context manager implementing __call__ (callable object).
# wrapper function uses our suppress object (that with self is using our object as a context manager)
# to wrap the call to our original function with the arguments that have been provided to us.'''
#     def __init__(self, *exc_types):
#         self.exc_types = exc_types
#
#     def __call__(self, function):
#         @wraps(function)
#         def wrapper(*args, **kwargs):
#             with self:
#                 return function(*args, **kwargs)
#         return wrapper
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exception, traceback):
#         self.exception = exception
#         self.traceback = traceback
#         if isinstance(exception, self.exc_types):
#             return True
#
#         return False


from contextlib import contextmanager


class ExceptionInfo:
    exception = None
    traceback = None


@contextmanager
def suppress(*exc_types):
    """Generator based Context manager that suppresses exceptions of given types."""
    info = ExceptionInfo()
    try:
        yield info
    except exc_types as exc:
        info.exception = exc
        info.traceback = exc.__traceback__
