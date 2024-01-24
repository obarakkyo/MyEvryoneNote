from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.mnvoice_base, name="mnvoice_base")
]
