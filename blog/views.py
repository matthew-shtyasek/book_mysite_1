from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:  # если индекс больше, чем кол-во страниц
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts
    }
    return render(request, template_name='blog/post/list.html', context=context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='p',
                             publish__year=year, publish__month=month, publish__day=day)
    return render(request, template_name='blog/post/detail.html', context={'post': post})
