from rest_framework import serializers
from details.models import *

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    apps = AppSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'apps', 'is_admin', 'is_underage', 'image']