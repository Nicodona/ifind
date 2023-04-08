from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoundItems.as_view(), name='found'),
    path("register/<int:pk>/", views.User_data.as_view(), name='found'),
    path('found', views.CreatItem.as_view(), name='founditem'),
    path('user/', views.UserCreate.as_view(), name='user'),
    path('login/', views.LoginView.as_view(), name='login')
]