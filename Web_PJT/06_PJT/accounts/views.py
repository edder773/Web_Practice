from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as account_login
from django.contrib.auth import logout as account_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_POST
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            account_login(request, form.get_user())
            return redirect('boards:index')
    else :
        form = AuthenticationForm()
    context = {'form' : form}
    return render(request, 'accounts/login.html',context)

def logout(request):
    account_logout(request)
    return redirect('boards:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_user_model().objects.get(pk=user_pk)
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    else:
        return redirect('accounts/login')
    
def profile(request, username):
    user = get_user_model().objects.get(username=username)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)
