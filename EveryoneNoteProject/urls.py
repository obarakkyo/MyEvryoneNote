from django.contrib import admin
from django.urls import path, include

"""media用の設定"""
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lecture/', include('lecture.urls')),
    path('mnvoice/', include('mnvoice.urls')),
    path('note/', include('note.urls')),
    path('upload/', include('upload.urls')),
    path('userlogapp/', include('userlogapp.urls')),
]

#開発の時はこれを記入する
if settings.DEBUG:
    urlpatterns+= static( settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
