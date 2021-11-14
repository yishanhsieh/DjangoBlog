from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
import markdown


def bloghome2(request):
    post_list = Post.objects.filter(status=1).order_by('-created_at')
    return render(request, 'bloghome2.html', {'post_list':post_list})

def about(request):
    return render(request, 'about.html', {})
    


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model = Post
    template_name =  'add_post.html'
    fields = '__all__'


