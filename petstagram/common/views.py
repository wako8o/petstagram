from django.shortcuts import render

# Create your views here.

def home_common(request):
    return render(request, 'common/home-page.html')
