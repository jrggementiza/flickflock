from django.urls import path

from . import views as flockstream_views

from django.conf import settings
from django.conf.urls.static import static

app_name = "flockstream"
urlpatterns = [
    path('', flockstream_views.index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)