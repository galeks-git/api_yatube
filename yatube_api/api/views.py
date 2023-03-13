# from django.shortcuts import render

# Create your views here.
#  импортируйте в код всё необходимое
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsOwnerOrReadOnly
from http import HTTPStatus

class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    serializer_class = CommentSerializer

    # def get_post(self):
    #     return get_object_or_404(
    #         Post, pk=self.kwargs.get('post_id')
    #     )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    # def perform_update(self, serializer):
    #     if serializer.instance.author != self.request.user:
    #         raise PermissionDenied()
    #         # raise PermissionDenied('Изменение чужого контента запрещено!', code=HTTPStatus.FORBIDDEN)
    #     # serializer.save()
    #     super(CommentViewSet, self).perform_update(serializer)

    # def perform_destroy(self, instance):
    #     # instance = self.get_object()
    #     if instance.author != self.request.user:
    #         raise PermissionDenied()
    #         # raise PermissionDenied('Изменение чужого контента запрещено!', code=HTTPStatus.FORBIDDEN)
    #     # serializer.delete()
    #     super(CommentViewSet, self).perform_destroy(instance)
    #     # self.perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
