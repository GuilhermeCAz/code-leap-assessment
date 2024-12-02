from typing import ClassVar

from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields: ClassVar = [
            'id',
            'username',
            'title',
            'content',
            'created_datetime',
        ]
