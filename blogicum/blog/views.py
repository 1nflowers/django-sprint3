from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post

POST_LIMIT = 5


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.published().with_related()[:POST_LIMIT]
    context = {'post_list': post_list}

    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )

    post_list = category.category_posts.published().with_related()
    template = 'blog/category.html'
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.published().with_related(),
        pk=post_id
    )
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)
