from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from .models import Post
# from .forms import PostForm


class PostList(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-published_date')
        return context


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'text', 'published_date']

    def form_valid(self, form):
        if self.request.user.is_anonymous():
            form.instance.author = User.objects.get(username='Anonymous')
        else:
            form.instance.author = self.request.user
        form.instance.created_date = timezone.now()
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostUpdate(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'text', 'published_date']

    def form_valid(self, form):
        if self.request.user.is_anonymous():
            form.instance.author = User.objects.get(username='Anonymous')
        else:
            form.instance.author = self.request.user
        return super(PostUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog/post_list')

    def get_success_url(self):
        return reverse('post_list')
