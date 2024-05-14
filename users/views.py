from django.shortcuts import render

# Create your views here.
def login(request):
    context={
        'title':'Home - Авторизация'
    }
    return render(request, 'login.html', context)


def registration(request):
    context={
        'title':'Home - Регистрация'
    }
    return render(request, 'registration.html', context)


def logout(request):
    ...
