from django.urls import path
from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.text_share, name='cart'),
]