from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . import forms
def index(request):
    return render(request, 'mainapp/index.html', {})


def login_user(request):

    username_error = ''
    password_error = ''
    message = ''


    if request.method == 'POST':
        if request.POST['username'] == None:
            username_error = 'вы должны указать псевдоним'
            return render(request, 'mainapp/login.html', {'message': username_error})
        if request.POST['password'] == None:
            password_error = 'вы должны указать пароль'
            return render(request, 'mainapp/login.html', {'message': password_error})

        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('/accounts/profile', request=request)

        return render(request, 'mainapp/login.html', {'message': 'Такого пользователя не существует'})
    return render(request, 'mainapp/login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('/', request=request)


def registration(request):

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/accounts/profile/', request=request)
        else:
            return render(request, 'mainapp/register.html', {'uform': form})
    form = forms.RegisterForm()
    return render(request, 'mainapp/register.html', {'uform': form})


@login_required
def user_cab(request):
    return render(request, 'mainapp/user_cab.html', {})


@login_required
def change_pass(request):
    if request.method == 'POST':
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password != conf_password:
            return render(request, 'mainapp/change_pass.html', {'message_err':'*Пароли должны совпадать'})
        user = request.user
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('/usercab', request=request)
    return render(request, 'mainapp/change_pass.html', {})

