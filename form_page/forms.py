from django import forms
from .models import Document



class ContactForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('COMPANY_NAME', 'FRONT_INSIDE_PICTURE','BUSINESS_CARD_IMAGE')
