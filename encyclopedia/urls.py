from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name='entry'),
    path("error", views.entry, name='error'),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("createpage", views.createpage, name="createpage"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("saveedit", views.saveedit, name="saveedit"),
    path("randompage", views.randompage, name="randompage")
]
