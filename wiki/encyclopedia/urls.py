from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entrys, name = "entrys"),
    path("search", views.searchbar, name = "searchbar")
]
