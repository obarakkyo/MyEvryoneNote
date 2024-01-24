from django.urls import path, include
from . import views

app_name = 'note_app'
urlpatterns = [
    path('<str:lecture_name>/', views.note_base, name="note_base")
]
