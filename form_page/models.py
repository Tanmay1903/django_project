'''
from __future__ import unicode_literals
from django.db import models

class Document(models.Model):
    COMPANY_NAME = models.CharField(max_length=255, blank=True)
    FRONT_INSIDE_PICTURE= models.FileField(upload_to='documents/')
    BUSINESS_CARD_IMAGE = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
'''
#'''
from mongoengine import *
from mongodbforms import DocumentForm
from datetime import datetime
import os
import json

#connect('Form1', alias='default')
connect(
    db= "Form2",
    username= "Tanmay1903",
    password= "Tanmaymongodb",
    host='mongodb+srv://Tanmay1903:Tanmaymongodb@intern-9eye-at0b4.mongodb.net/Form2?retryWrites=true&w=majority',
)

class Form_content(Document):
    COMPANY_NAME = StringField(max_length=200, required=True)
    FRONT_INSIDE_PICTURE = FileField()
    BUSINESS_CARD_IMAGE = FileField()
    uploaded_at = DateTimeField(default=datetime.utcnow)

def json(self):
    form_dict= {
    "COMPANY_NAME" : self.COMPANY_NAME,
    "FRONT_INSIDE_PICTURE" : self.FRONT_INSIDE_PICTURE,
    "BUSINESS_CARD_IMAGE" : self.BUSINESS_CARD_IMAGE,
    }
    return json.dumps(form_dict)
#'''
disconnect()
