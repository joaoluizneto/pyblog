from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'website'
urlpatterns = [
    # ex: /website/
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)