# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import include, path
# from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

# from api.views import PostViewSet
from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = routers.DefaultRouter()
# api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
# api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
router.register('posts', PostViewSet)
# api/v1/groups/ (GET): получаем список всех групп.
# api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
router.register('groups', GroupViewSet)
# router.register(r'achievements', AchievementViewSet)
router.register(
    # r'^posts/(?P<post_id>\d+)/comments/$',
    r'posts/(?P<post_id>\d+)/comments',
    # r'posts/(?P<post_id>\d+)/comments',
    # 'posts/<post_id>/comments/',
    CommentViewSet,
    basename='comments'
)
# #  импортируйте в код всё необходимое
# from django.urls import include, path
# from rest_framework import routers

# from .views import PostViewSet

# router = routers.DefaultRouter()
# router.register('api/v1/posts', PostViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', include(router.urls)),
    # api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
    path('api-token-auth/', views.obtain_auth_token),
    # api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
    # api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
]
