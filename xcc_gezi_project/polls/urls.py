from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path("add_food/", views.add_food),
    path("select_food/", views.select_food),
    path("update_food/", views.update_food),
    path("delete_food/", views.delete_food),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]