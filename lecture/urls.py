from django.urls import path, include
from . import views

app_name = 'lecture_app'

urlpatterns = [
    path('', views.lecture_base, name="lecture_base")
]
