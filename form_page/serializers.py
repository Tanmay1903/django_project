from rest_framework_mongoengine import serializers
from .models import Form_content

class Form_contentSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Form_content
        fields =  ('COMPANY_NAME', 'FRONT_INSIDE_PICTURE','BUSINESS_CARD_IMAGE')
