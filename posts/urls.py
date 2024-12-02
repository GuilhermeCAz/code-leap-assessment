from django.urls import path

from posts.views import PostCollectionView, PostItemView

urlpatterns = [
    path('', PostCollectionView.as_view(), name='post-collection'),
    path('<int:pk>/', PostItemView.as_view(), name='post-item'),
]
