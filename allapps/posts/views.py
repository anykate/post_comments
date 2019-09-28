from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    post_form = None
    posts = Post.objects.all()
    admin = User.objects.filter(is_staff=True).first()

    # Only if at least 1 superuser exists, show the form to create posts and add the
    # superuser as the default author for all posts.
    # You may add a different logic for adding the form to create posts
    if admin:
        post_form = PostForm(data=request.POST or None)
        if post_form.is_valid():
            this_post = post_form.save(commit=False)
            this_post.author = admin
            this_post.save()
            return redirect('posts:index')

    return render(request, 'posts/index.html', {'posts': posts, 'post_form': post_form, 'admin': admin})


def post_detail(request, post):
    this_post = get_object_or_404(Post, slug=post)
    comments = this_post.comment_set.filter(active=True)
    new_comment = None
    comment_form = CommentForm(data=request.POST or None)

    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = this_post
        new_comment.save()
        messages.info(
            request,
            f'Dear \"{new_comment.name}\", your comment has been added, however, it '
            'is pending with admin for approval. Once approved, it will appear '
            'in this post\'s comments section !!'
        )
        return redirect('posts:post_detail', this_post.slug)

    context = {'post': this_post, 'comments': comments,
               'new_comment': new_comment, 'comment_form': comment_form}

    return render(request, 'posts/detail.html', context)
