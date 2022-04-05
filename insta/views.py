
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from insta import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from insta.models import Comments, Post, Profile, UserFollowing
from .forms import CommentForm, UserRegistrationForm, PostForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm

    return render(request, 'index.html', {'form': form, 'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(
            #     request, f'Account for {username} created, please log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/registration.html', {'form': form})

# def profile(request):
#     update_form = UpdateProfileForm()
#     profile_form = UpdateProfileForm()
#     context = {
#         'u_form':update_form,
#         'p_form':profile_form,
#     }
    
#     return render(request, 'profile.html', context)



class PostListView(ListView):
    models = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-posted_on']

    def get_queryset(self):
        return models.Post.objects.all()


class PostDetailView(DetailView):
    models = Post

    def get_queryset(self):
        return models.Post.objects.all()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'name', 'caption']

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'add_comments.html'

    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image', 'name', 'caption']

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.profile:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.profile:
            return True
        return False


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(profile=user)

        # followers = profile.followers.all()
        # followers = UserFollowing.objects.values_list('following_user_id')
        followers = UserFollowing.objects.filter(following_user_id=pk)
        following = UserFollowing.objects.filter(user_id=pk)

        # if len(following) == 0:
        #     status = True
        status = None

        for follower in followers:
            print(follower.user_id.username)
            print(request.user.username)
            if follower.user_id.username == request.user.username:
                status = True
                break
            else:
                status = False

        TotalFollowers = len(followers)
        TotalFollowing = len(following)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'TotalFollowers': TotalFollowers,
            'TotalFollowing': TotalFollowing,
            'status': status,
        }
        return render(request, 'profile.html', context=context)


class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = get_object_or_404(User, pk=pk)
        UserFollowing.objects.create(user_id=request.user,
                                     following_user_id=user)

        return redirect('profile', pk=profile.pk)


class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = get_object_or_404(User, pk=pk)
        UserFollowing.objects.filter(user_id=request.user,
                                     following_user_id=user).delete()

        return redirect('profile', pk=profile.pk)
