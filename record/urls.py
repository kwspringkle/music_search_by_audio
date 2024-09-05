from django.urls import path
from . import views

urlpatterns=[
    path('record', views.record_audio_file, name="record" ),
]