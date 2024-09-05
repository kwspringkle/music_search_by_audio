from django.urls import path
from .views import default_view
from . import views

urlpatterns=[
    path('', default_view, name="home"),
    path('upload', views.upload_audio_file, name="upload" ),
    path('search/<path:audio_path>', views.search, name='search'),
]