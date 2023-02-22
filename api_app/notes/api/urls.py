from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes', views.getNote, name="notes"),
    path('notes/create', views.createNote, name="create"),
    path('notes/<int:pk>/', views.getDetail, name="note"),
    path('notes/update/<int:pk>/', views.updateNote, name="update"),
    path('notes/delete/<int:pk>/', views.deleteNote, name="delete"),
]