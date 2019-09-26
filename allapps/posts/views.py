from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


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
            f'Your comment: \"{new_comment.body}\" has been added & '\
            'is now pending with admin for approval !!'
        )
        return redirect('posts:post_detail', this_post.slug)

    context = {'post': this_post, 'comments': comments,
               'new_comment': new_comment, 'comment_form': comment_form}

    return render(request, 'posts/detail.html', context)
