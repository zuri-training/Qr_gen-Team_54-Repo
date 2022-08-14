from django.shortcuts import redirect



def unauthenticated_user(view_funct):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("qrcode_options")
        return view_funct(request, *args, **kwargs)
    return wrapper_func