from functools import wraps

from django.core import exceptions


def user_passes_test(test_func):
    def decorator(f):
        @wraps(f)
        def wrapper(request, *args, **kwargs):
            if test_func(request.user):
                return f(request, *args, **kwargs)
            raise exceptions.PermissionDenied()
        return wrapper
    return decorator


login_required = user_passes_test(lambda u: u.is_authenticated)
