from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

#app_name = 'users'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:users_id>', views.profile, name='profile'),
    path('<int:users_id>/', views.profile, name='profile'),

    path('members/', views.members, name='members'),

    path("logout/", LogoutView.as_view(), name="logout"),
    path('update_profile', views.update_profile, name='update_profile'),
    #path('update_profile/<int:users_id>/', views.update_profile, name='update_profile'),

]