from django.urls import path, include
from . import views

app_name = "upload_app"

urlpatterns = [
    path('<str:lecture_name>/', views.upload_base, name="upload_base")
]
