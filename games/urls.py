from . import views
from django.urls import path
from .views import (
    post_game_view,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostList,
    PostDetail,
    PostLike,
    post_game,
    delete_post,
    addGame,
    post_game_view
)

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('delete/<post_id>', delete_post, name='delete'),
    path('post_game/', post_game, name='post_game'),
    path('add_game/', addGame, name='add_game'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post_game_view/', post_game_view, name='post_game_view'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),
]
