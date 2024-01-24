from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lecture/', include('lecture.urls')),
    path('mnvoice/', include('mnvoice.urls')),
    path('note/', include('note.urls')),
    # path('upload/', include('upload.urls')),
    # path('userlogapp/', include('userlogapp.urls')),
]
