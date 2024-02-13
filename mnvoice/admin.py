from django.contrib import admin
from .models import BoardModel, SyllabusModel
# Register your models here.

admin.site.register(BoardModel)
admin.site.register(SyllabusModel)