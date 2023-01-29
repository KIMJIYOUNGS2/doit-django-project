from django.shortcuts import render


def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )
