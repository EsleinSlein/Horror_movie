from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesList.as_view(), name='home'),
    path('add_movie', views.AddMovie.as_view(), name='add_movie'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout')
]
