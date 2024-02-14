from django.urls import path, include
from . import views

app_name = "userlogapp"
urlpatterns = [
    path('', views.userlogapp_base, name="login"),
    path('search/', views.SearchFunction, name="search"),
    path('signup/', views.signupfunc, name="signup"),
    path('logout/', views.logoutfunc, name="logout"),
    path('base/', views.base_func, name="base"),
    path('lecture_lists/', views.lecture_lists_func, name="lecture_lists")
]
