# from django.shortcuts import render

# Create your views here.
#  импортируйте в код всё необходимое
from rest_framework import viewsets
from rest_framework import generics
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class MessageList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_id'])
    # def get_queryset(self):
    #     return Post.objects.get(pk=self.kwargs['post_id']).comment_set.all()

    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # @action(detail=False, url_path='comments')
    # def comments(self, request):
    #     # Нужны только последние пять котиков белого цвета
    #     cats = Cat.objects.filter(color='White')[:5]
    #     # Передадим queryset cats сериализатору 
    #     # и разрешим работу со списком объектов
    #     serializer = self.get_serializer(cats, many=True)
    #     return Response(serializer.data) 
    # @action(detail=True)
    # def comments(self, request, pk=None):
    # post = self.get_object()
    # comments = post.comment_set.all()
    # serializer = CommentSerializer(comments, many=True)

    # return Response(serializer.data)

# class GroupViewSet(viewsets.ModelViewSet):
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
