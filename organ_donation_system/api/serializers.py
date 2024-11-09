from rest_framework import serializers
from .models import donors
from .models import recipients

class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = recipients
        fields = ['full_name', 'email', 'contact_number', 'date_of_birth', 'gender', 'blood_group', 'organ_needed', 'address']
        

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = donors
        fields = ['full_name', 'email', 'contact_number', 'date_of_birth', 'gender', 'blood_group', 'organ_to_donate', 'address']
        
