from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
import datetime


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        title = self.title
        year = str(datetime.datetime.now().date().year)

        # month = str(datetime.datetime.now().date().month)
        month = str(datetime.datetime.now().date().strftime("%m"))

        # day = str(datetime.datetime.now().date().day)
        day = str(datetime.datetime.now().date().strftime("%d"))

        # hour = str(datetime.datetime.now().hour)
        hour = str(datetime.datetime.now().strftime("%H"))

        # minute = str(datetime.datetime.now().minute)
        minute = str(datetime.datetime.now().strftime("%M"))

        # second = str(datetime.datetime.now().second)
        second = str(datetime.datetime.now().strftime("%S"))

        time = year + ' ' + month + ' ' + day + \
            ' ' + hour + ' ' + minute + ' ' + second

        self.slug = slugify(title + ' ' + time)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
