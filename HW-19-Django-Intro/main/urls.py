from django.urls import path
from .views import IndexViewClass

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", IndexViewClass.as_view(), name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
