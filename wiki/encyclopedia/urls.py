from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entrys, name = "entrys"),
    path("search", views.searchbar, name = "searchbar"),
    path("newpage", views.create, name = "create"),
    path("editpage/<str:result>", views.edit, name = "edit"),
    path("random", views.random_page, name = "random_page")
]
