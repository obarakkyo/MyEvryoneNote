from django.urls import path, include
from . import views

app_name = 'note_app'
urlpatterns = [
    path('<str:lecture_name>/<str:lecture_number>/<int:page_number>', views.note_base, name="note_base"),
    path('next/<str:lecture_name>/<str:lecture_number>/<int:page_number>', views.note_next_page, name="note_next_page"),
    path('previous/<str:lecture_name>/<str:lecture_number>/<int:page_number>', views.note_previous_page, name="note_previous_page"),
]
