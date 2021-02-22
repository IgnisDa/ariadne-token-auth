from functools import wraps

from . import exceptions


def user_passes_test(test_func):
    def decorator(f):
        @wraps(f)
        def wrapper(request, *args, **kwargs):
            if test_func(request.user):
                return f(request, *args, **kwargs)
            raise exceptions.PermissionDenied()

        return wrapper

    return decorator


def context(f):
    def decorator(func):
        def wrapper(*args, **kwargs):
            info = args[f.__code__.co_varnames.index("info")]
            return func(info.context, *args, **kwargs)

        return wrapper

    return decorator


def user_passes_test_ariadne(test_func):
    def decorator(f):
        @wraps(f)
        @context(f)
        def wrapper(context, *args, **kwargs):
            if test_func(context.get("request").user):
                return f(*args, **kwargs)
            raise exceptions.PermissionDenied()

        return wrapper

    return decorator


login_required = user_passes_test(lambda u: u.is_authenticated)
login_required_ariadne = user_passes_test_ariadne(lambda u: u.is_authenticated)
