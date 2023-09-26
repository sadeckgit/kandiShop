from django.urls import path

from knox.views import LogoutView, LogoutAllView
from .import views


urlpatterns = [
    path('sign-up/', views.CreateUserAPI.as_view()),
    path('update-user/', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout/', LogoutAllView.as_view()),
]
