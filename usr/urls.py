from django.urls import path
from . import views

app_name = 'usr'
urlpatterns = [
    path('', views.sessionView, name='sessionview'),
]