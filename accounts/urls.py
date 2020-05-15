from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('signup/',SignUpView.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name = 'accounts/login.html' ),name= 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('profile/<str:username>/',get_profile,name = 'profile'),
    path('create_profile/',CreateProfileView.as_view(),name = 'create_profile'),
    path('update_profile/',UpdateProfileView.as_view(),name = 'update_profile')

]
