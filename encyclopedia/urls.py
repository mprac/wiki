from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name='entry'),
    path("error", views.entry, name='error'),
    path("search", views.search, name="search")
]
