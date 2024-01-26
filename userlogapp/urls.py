from django.urls import path, include
from . import views

app_name = "userlogapp"
urlpatterns = [
    path('', views.userlogapp_base, name="login"),
    path('search/', views.SearchFunction, name="search"),
    path('signup/', views.signupfunc, name="signup")
]
