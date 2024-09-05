from django.shortcuts import render, redirect
import requests
import os
from .models import uploaded_audio
from django.http import JsonResponse
from django.urls import reverse
# Create your views here.
API_KEY= os.environ['API_KEY']

def default_view(request):
    return render(request, 'index.html')

def upload_audio_file(request):
    if request.method == "POST":
        uploaded_audio_name = request.POST.get('uploaded_audio_name')
        audio_file = request.FILES['audio_file']
        
        print(f"File saved at: {audio_file}")
        uploaded_audio_obj = uploaded_audio(
            uploaded_audio_name=uploaded_audio_name,
            path=audio_file
        )
        uploaded_audio_obj.save()
        audio_path = f"media/uploaded_audio/{audio_file}"
        return redirect(reverse('search', kwargs={'audio_path': audio_path}))
    return render(request, 'index.html')

def search(request, audio_path):
    try:
        data = {
            'api_token': API_KEY,
            'return': 'apple_music, spotify',
        }
        files = {
            'file': open(audio_path, 'rb')
        }
        result = requests.post('https://api.audd.io/', data=data, files=files)
        files['file'].close()
        
        print(result.text)
        return render(request, 'search_result.html', {'result': result.json()})
    
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found.'}, status=404)
