from . import views
from django.urls import path

app_name = 'priiist_app'

urlpatterns = [
    # home page
    path('', views.index, name = 'index'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
]