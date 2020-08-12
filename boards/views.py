from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
import datetime
# We write .models, cause models is in the same directory.

@login_required(login_url = 'login')
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'boards/home.html',context)

def about(request):
    return render(request,'boards/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'boards/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'boards/post_detail.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    datetime = datetime.datetime.now()

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_posted = self.datetime
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    datetime = datetime.datetime.now()

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_posted = self.datetime
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False





""""views are functions that receive Request as a parameter and return response as a result. Basically they 
    receive HttpRequest object and returns HttpResponse object"""

'''There are class based views and there are function based views, here we will be using class based views for 
    doing lots of operations, like create, update or delete posts etc. Class-based views provide an alternative way to 
    implement views as Python objects instead of functions. They do not replace function-based views, but have 
    certain differences and advantages when compared to function-based views:

Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods 
    instead of conditional branching.
Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable
    components.'''

