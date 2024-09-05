from django.db import models

# Create your models here.
class uploaded_audio(models.Model):
    uploaded_audio_name=models.TextField(null=True)
    path=models.FileField(upload_to='uploaded_audio/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uploaded_audio_name} created at {self.created_at}"
    
     