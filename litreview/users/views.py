from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from . import forms


# Create your views here.
def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'registration succ')
            return redirect('account')
    else:
        form = UserCreationForm()
        messages.warning(request, 'There is a problem')
    return render(request, 'users/register.html', {'form':form})

# Create your views here.
def login_user(request):
    form = forms.LoginForm

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account')
            else:
                messages.success(request, ("there was an erro logging please check data"))
                return redirect('users/login.html')
    else:
        return render(request, 'users/login.html', context={'form': form})


