from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingViews, name="landing"),
]