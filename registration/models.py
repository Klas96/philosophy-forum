from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SocialMediaConnection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)  # e.g., 'Facebook'
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    expires_in = models.DateTimeField()  # When the access token expires

    def __str__(self):
        return f"{self.user.username} - {self.platform}"

