from django.contrib import admin
from django.urls import include, path
from .views import homepage
from . import views

urlpatterns = [
    path("", homepage, name="homepage"),
    path("", views.Insertrecord),
]
