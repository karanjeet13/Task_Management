from functools import wraps
from data.standard_response import UnauthorizedAccessResponse

def access_control_decorator(allowed=[]):
    def decorator(view_function):
        @wraps(view_function)
        def wrapper_func(self, request, *args, **kwargs):
            if request.employee.user_type in allowed:
                return view_function(self, request, *args, **kwargs)
            else:
                return UnauthorizedAccessResponse('You are not Authorized!')
        return wrapper_func
    return decorator
