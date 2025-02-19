from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.FeedView.as_view(), name='feed'),
        path('posts/<int:pk>/like/', views.LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike-post'),

]
rom django.urls import path
from .views import FeedView

urlpatterns = [
    # ...
    path('feed/', FeedView.as_view(), name='feed'),
]