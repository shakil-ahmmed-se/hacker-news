from django.shortcuts import render
from .serializers import StorySerializer
from rest_framework import generics, status
from rest_framework.views import APIView
import requests
from datetime import datetime
from rest_framework.response import Response
from .models import Story
# Create your views here.

class TopStoriesView(APIView):
    def get(self, request):
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(url)
        story_ids = response.json()
        stories = []
        for story_id in story_ids:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story_response = requests.get(story_url)
            story_data = story_response.json()
            story_data['story_id'] = story_id
            stories.append(story_data)
            if len(stories) >= 10:
                break
        serializer = StorySerializer(stories, many=True)
        return Response(stories, status=status.HTTP_200_OK)
    

    





