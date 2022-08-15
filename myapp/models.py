from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=255)
    email_id = models.EmailField(max_length=255, unique=True)
    doubtquery = models.CharField(max_length=255)

class Document(models.Model):
    about=models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    file=models.FileField(upload_to="gallery/", max_length=250, null=True, default=None)
    doc_status= models.CharField(max_length=1, default='0')
    doc_owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_by', verbose_name='Owner')
