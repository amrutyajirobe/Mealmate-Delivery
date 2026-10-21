from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('open_home/', views.hello, name='open_home'),
    path('open_signup/', views.open_signup, name='open_signup'),
    path('signup/', views.signup, name='signup'),
    path('open_signin/', views.open_signin, name='open_signin'),
    path('signin/', views.signin, name='signin'),
]
