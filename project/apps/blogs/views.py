from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View, CreateView

from braces.views import LoginRequiredMixin
from blogs.forms import PostCreateForm

from blogs.models import Post, Blog, PostReadMark


class UserFeedView(LoginRequiredMixin, ListView):
    template_name = u'feed.html'
    model = Post
    context_object_name = u'posts'

    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.for_user(user)
        return posts


class PostDetailView(DetailView):
    template_name = u'posts/detail.html'
    context_object_name = u'post'
    model = Post


class PostMarkAsReadView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        raise Http404

    def get_post(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return

    def post(self, request, *args, **kwargs):
        post = self.get_post(kwargs.get(u'pk', 0))
        if not post:
            raise Http404
        post_read_mark, created = PostReadMark.objects.get_or_create(
            user=request.user,
            post=post
        )
        if not created:
            post_read_mark.is_read = True
            post_read_mark.save()
        messages.success(request, u'Successfully marked as read!')
        return HttpResponseRedirect(post.get_absolute_url())


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = u'posts/new.html'
    model = Post
    form_class = PostCreateForm

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs[u'blog'] = self.request.user.blog
        return kwargs

    def form_valid(self, form):
        post = form.save()
        PostReadMark.objects.create(
            user=self.request.user,
            post=post
        )
        return HttpResponseRedirect(post.get_absolute_url())


class BlogListView(ListView):
    template_name = u'blogs/list.html'
    model = Blog
    context_object_name = u'blogs'


class BlogDetailView(DetailView):
    template_name = u'blogs/detail.html'
    model = Blog
    context_object_name = u'blog'


class BlogSubscribeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        raise Http404

    def get_blog(self, blog_id):
        try:
            return Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return

    def post(self, request, *args, **kwargs):
        blog = self.get_blog(kwargs.get(u'pk', 0))
        if not blog:
            raise Http404

        if request.user in blog.subscribers.all():
            blog.subscribers.remove(request.user)
            message = u'Successfully unsubscribed!'
        else:
            blog.subscribers.add(request.user)
            message = u'Successfully subscribed!'
        messages.success(request, message)
        return HttpResponseRedirect(reverse(u'blogs:list'))
