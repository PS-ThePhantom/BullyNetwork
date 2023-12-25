from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    siteName = models.CharField(max_length=50, default='Bully Network')