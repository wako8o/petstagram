from django.shortcuts import render

# Create your views here.

def log_accounts(request):
    return render(request, 'accounts/login-page.html')

def register_accounts(request):
    return render(request, 'accounts/register-page.html')

def edit_accounts(request, pk):
    return render(request, 'accounts/profile-edit-page.html')

def delete_accounts(request, pk):
    return render(request, 'accounts/profile-delete-page.html')

def details_accounts(request, pk):
    return render(request, 'accounts/profile-details-page.html')