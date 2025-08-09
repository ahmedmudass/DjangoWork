from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("a", views.About_page, name="about"),
    path("c", views.Contact_Page, name="con"),
]