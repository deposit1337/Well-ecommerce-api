from django.urls import path,include
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
