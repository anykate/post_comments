from django import forms
from .models import Post, Comment
from .utils import calc_slug


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['slug'].disabled = True
        self.fields['slug'].required = False
        self.fields['slug'].initial = 'this-field-will-be-saved-automatically-to-database'

    class Meta:
        model = Post
        fields = ('title', 'slug', 'body',)

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        title = self.cleaned_data['title']
        slug = calc_slug(title)
        return slug


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)
