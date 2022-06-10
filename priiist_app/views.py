from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'priiist_app/index.html')


def portfolio_details(request):
    return render(request, 'priiist_app/portfolio_details.html')
