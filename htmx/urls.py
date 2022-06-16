from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
 
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("check-username/", views.check_username, name='check-username'),
 
]