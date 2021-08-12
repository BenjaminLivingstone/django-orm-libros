from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addbook/', views.addbook),
    path('authors/', views.author),
    path('addauthor/', views.addauthor),
    path('books/<int:num>', views.addbook),
    path('authors/<int:num>', views.addauthor),

]