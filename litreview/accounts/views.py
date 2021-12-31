from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def account(request):
    context = {}
    return render(request, 'accounts/account.html')