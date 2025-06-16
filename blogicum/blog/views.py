from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Category, Post

current_time = timezone.now()


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related('author', 'location', 'category').filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    ).order_by('-pub_date')

    template = 'blog/category.html'
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__lte=current_time,
            is_published=True,
            category__is_published=True
        ),
        pk=post_id
    )
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)
