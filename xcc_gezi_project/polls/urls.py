from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path("add_food/", views.add_food),
    path("select_food/", views.select_food),
    path("update_food/", views.update_food),
    path("delete_food/", views.delete_food),
]