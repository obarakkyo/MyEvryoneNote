from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.note_base, name="note_base")
]
