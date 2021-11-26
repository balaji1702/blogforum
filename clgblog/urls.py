

from django.urls import path

from . import views




urlpatterns = [
    path('list/', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    
]