from .models import Comment, Post, Games
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'featured_image',
            'excerpt',
            'content',
            'status',
            'likes',
        )

        def __init__(self, *args, **kwargs):
            super(PostGames, self).__init__(*args, **kwargs)


class GameForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'

    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            # 'author',
            'featured_image',
            'excerpt',
            'content',
            'status',
            # 'likes'
        )

        def __init__(self, *args, **kwargs):
            super(PostGames, self).__init__(*args, **kwargs)


class PostGameForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
