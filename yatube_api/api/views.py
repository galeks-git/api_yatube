# from django.shortcuts import render

# Create your views here.
#  импортируйте в код всё необходимое
from rest_framework import viewsets

from posts.models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
