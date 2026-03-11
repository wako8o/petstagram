from django.shortcuts import render

# Create your views here.

def accounts_log(request):
    return render(request, 'accounts/login-page.html')