from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.userlogapp_base, name="login"),
    path('search/', views.SearchFunction, name="search")
]