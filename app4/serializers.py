from rest_framework import serializers
from app2.models import login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'
