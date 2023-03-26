from django.shortcuts import render,redirect
from django.contrib.auth import login as account_login
from django.contrib.auth import logout as account_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomedUserCreationForm, CustomedUserChangeForm

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            account_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    content = {'form' : form}
    return render(request,'accounts/login.html',content)

def logout(request):
    account_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('articles:index')
    else:
        # form = CustomedUserCreationForm()
    content = {'form' : form}
    return render(request, 'accounts/signup.html',content)

def unregister(request):
    request.user.delete() #탈퇴 후
    account_logout(request) # 로그아웃 순으로 꼭 진행
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomedUserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomedUserChangeForm()
    content = {'form' : form}
    return render(request, 'accounts/update.html', content)

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    content = {'form':form}
    return render(request, 'accounts/password_change.html',content)