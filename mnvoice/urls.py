from django.urls import path, include
from . import views

app_name = "mnvoice_app"

urlpatterns = [
    path('<str:lecture_name>/', views.mnvoice_base, name="mnvoice_base")
]
