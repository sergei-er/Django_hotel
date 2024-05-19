from django.shortcuts import render
from django.contrib import auth
from users.forms import UserLoginForm, UserRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if  user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm

    context={
        'title':'Home - Авторизация',
        'form': form
    }
    return render(request, 'login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context={
        'title':'Home - Регистрация',
        'form': form
    }
    return render(request, 'registration.html', context)


def logout(request):
    return HttpResponseRedirect(reverse('main:index'))
