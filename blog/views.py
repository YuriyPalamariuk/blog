from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect

from .models import Post
# from .forms import PostForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save()
            # user.user_set.add()
            # Group.objects.get(name='blog').user_set.add(user)
            user.groups.add(Group.objects.get(name='blog'))

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})


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
