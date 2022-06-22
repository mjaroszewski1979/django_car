from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
 
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("check-username/", views.check_username, name='check-username'),
    path("cars/", views.CarList.as_view(), name="car_list"),
    path('add-car/', views.add_car, name='add_car'),
    path('delete-car/<int:id>/', views.delete_car, name='delete_car'),
    path('search-car/', views.search_car, name='search_car'),
    path('clear/', views.clear, name='clear'),
    path('sort/', views.sort, name='sort'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('car-list-partial', views.cars_partial, name='car_list_partial'),
    path('upload-photo/<int:id>/', views.upload_photo, name='upload_photo'),
 
]