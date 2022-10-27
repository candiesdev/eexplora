from django.urls import path
from . import views

urlpatterns = [
    path("", views.property, name="property"),
    path("<propertyCode>", views.property, name="property"),
]