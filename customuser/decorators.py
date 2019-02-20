from django.utils import translation


def check_lang(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if translation.LANGUAGE_SESSION_KEY in request.session:
                del request.session[translation.LANGUAGE_SESSION_KEY]
            translation.activate(request.user.language)
            request.session[translation.LANGUAGE_SESSION_KEY] = request.user.language
            return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
