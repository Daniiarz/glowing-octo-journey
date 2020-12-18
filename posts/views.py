from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from posts.forms import PostForm
from posts.models import Post


class PostsView(ListView):
    model = Post
    template_name = 'posts/index.html'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'


def add_post(httpRequest):
    method = httpRequest.method
    if method == "POST":
        form = PostForm(httpRequest.POST, httpRequest.FILES)
        Post.objects.create(
            title=form.data['title'],
            description=form.data['description'],
            image=form.data['image'],
            text=form.data['text']
        )
        return HttpResponse('Post created!')
    else:
        form = PostForm()

    return render(httpRequest, 'posts/add_post.html', {'form': form})
