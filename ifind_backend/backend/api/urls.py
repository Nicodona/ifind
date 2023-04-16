from django.urls import path
from . import views

urlpatterns = [
    #get routes
    path('', views.FoundItems.as_view(), name='found'),
    path('job/', views.JobItems.as_view(), name='job'),
    path('report/', views.Reports.as_view(), name='report'),
    path('messages/', views.Messages.as_view(), name='report'),

    #detail routes
    path("register/<int:pk>/", views.User_data.as_view(), name='detail_register '),
    path("found/<int:pk>/", views.FoundDetail.as_view(), name='found_det'),
    path("job/<int:pk>/", views.JobDetail.as_view(), name='job_det'),
    path("reg/<int:pk>/", views.User_data.as_view(), name='detail_register '),

    #post routes

    #forms
    path('found/', views.CreateItem.as_view(), name='founditem'),
    path('add_job/', views.CreateJob.as_view(), name='add_job'),
    path('add_register/', views.CreateProfile.as_view(), name='register'),
    path('add_message/', views.CreateMessage.as_view(), name='message'),
    path('add_report/', views.CreateReport.as_view(), name='register'),


    #auth
    path('user/', views.UserCreate.as_view(), name='user'),
    path('login/', views.LoginView.as_view(), name='login'),

]