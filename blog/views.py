from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect


def list(request):
    Data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, 'pages/blog/blog.html', Data)


def post(request, id):
    post = {'post': Post.objects.get(id=id)}
    return render(request, 'pages/blog/post.html', post)


def create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, 'pages/blog/create.html', {'form': form})
