from django.urls import path, include
from . import views

app_name = "upload_app"

urlpatterns = [
    path('<str:lecture_name>/<str:lecture_number>/', views.upload_base, name="upload_base")
]
