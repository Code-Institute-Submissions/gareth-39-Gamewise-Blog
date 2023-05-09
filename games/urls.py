from . import views
from django.urls import path
from .views import (
    post_games_view,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostList,
    PostDetail,
    PostLike,
    post_games,
    delete_post,
    addGames,
    post_games_view
)

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('delete/<post_id>', delete_post, name='delete'),
    path('post_games/', post_games, name='post_vehicle'),
    path('add_games/', addGames, name='add_vehicle'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post_games_view/', post_games_view, name='post_vehicle_view'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),
]
