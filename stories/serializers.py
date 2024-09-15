from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.Serializer):
    class Meta:
        model = Story
        fields = '__all__'
        
