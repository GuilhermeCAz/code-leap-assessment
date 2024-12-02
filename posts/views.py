from rest_framework import generics

from posts.models import Post
from posts.serializer import PostSerializer


class PostCollectionView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer


class PostItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
