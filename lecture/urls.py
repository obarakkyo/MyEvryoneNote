from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.lecture_base, name="lecture_base")
]
