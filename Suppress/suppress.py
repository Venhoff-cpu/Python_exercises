# from contextlib import contextmanager
#
# @contextmanager
# def suppress(error_type):
#     try:
#         yield
#     except:


class suppress:
    def __init__(self, error_type):
        self.error_type = error_type

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception, traceback):
        if isinstance(exception, self.error_type):
            return True

        return False
