from django.shortcuts import render, redirect
from django.contrib.auth import login as account_login
from django.contrib.auth import logout as account_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            account_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    content = {'form' : form}
    return render(request, "accounts/login.html", content)

def logout(request):
    account_logout(request)
    return redirect('movies:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    content = {'form' : form}
    return render(request, 'accounts/signup.html',content)

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm()
    content = {'form' : form}
    return render(request, 'accounts/update.html',content)

def delete(request):
    request.user.delete()
    account_logout(request)
    return redirect('movies:index')

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    content = {'form':form}
    return render(request, 'accounts/password_change.html',content)