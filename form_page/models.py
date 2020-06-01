from __future__ import unicode_literals
from django.db import models

class Document(models.Model):
    COMPANY_NAME = models.CharField(max_length=255, blank=True)
    FRONT_INSIDE_PICTURE= models.FileField(upload_to='documents/')
    BUSINESS_CARD_IMAGE = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
