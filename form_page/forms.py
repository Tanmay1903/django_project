'''
from django import forms
from .models import Document

class ContactForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('COMPANY_NAME', 'FRONT_INSIDE_PICTURE','BUSINESS_CARD_IMAGE')
'''
#'''
from django import forms
from .models import Form_content
#from django_mongoengine.forms import DocumentForm
from mongodbforms import DocumentForm

class ContactForm(DocumentForm):
    class Meta:
        document = Form_content
        fields = ('COMPANY_NAME', 'FRONT_INSIDE_PICTURE','BUSINESS_CARD_IMAGE')
#'''
