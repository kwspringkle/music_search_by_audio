from django.shortcuts import render, redirect
import os
from .models import recorded_audio
from django.urls import reverse
from upload.views import search
# Create your views here.

API_KEY = os.environ['API_KEY']

def record_audio_file(request):
    if request.method == "POST":
        recorded_audio_name = request.POST.get('recorded_audio_name')
        audio_file = request.FILES['audio_file']

        recorded_audio_obj = recorded_audio(
            recorded_audio_name=recorded_audio_name,
            path=audio_file
        )
        recorded_audio_obj.save()
        audio_path = f"media/recorded_audio/{audio_file}"
        return redirect(reverse('search', kwargs={'audio_path': audio_path}))

    return render(request, 'index.html')
