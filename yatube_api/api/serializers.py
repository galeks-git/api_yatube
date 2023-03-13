from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        # fields = (
        #     'id', 'text', 'pub_date', 'author', 'image', 'group'
        # )
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
        # fields = (
        #     'id', 'title', 'slug', 'description'
        # )
        # read_only_fields = ('slug',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post',)
        # fields = (
        #     'id', 'author', 'post', 'text', 'created'
        # )
        # read_only_fields = ('slug',)
