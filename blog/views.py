from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context import RequestContext
from .models import Post
from collections import OrderedDict
from itertools import chain
import json
import stripe
from django.conf import settings
import random
from advertisement.helper import getAds

from .models import *

def new_main(request):
    """Main listing."""

    themes = {}
    allThemes = ["critique", "echo", "hyperlink", "transcripts"]
    for theme in allThemes:
        posts = Post.objects.all().filter(theme__name=theme)
        # sort to get recent posts
        all_posts_sorted = list(reversed(sorted(posts, key=lambda i: i.created)))
        # choose randomly from 3 most recent
        if len(all_posts_sorted) > 0:
            themes[theme] = random.choice(all_posts_sorted[:3])

    data = {
        'themes': themes,
        # 'posts_data': list(blog_page)
    }

    template_name = 'blog_index.html'
    return render(request, template_name, data)


def main(request):
    """Main listing."""
    posts = Post.objects.all()
    all_posts_sorted = list(reversed(sorted(posts, key=lambda i: i.created)))
    blog_page = paginate_posts(request, all_posts_sorted)

    data = {
        'posts': blog_page,
        'posts_data': list(blog_page)
    }
    template_name = 'blog.html'
    data['ads'] = getAds('blog')
    return render(request, template_name, data)

def post(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    data = {
        'post': post
    }
    template_name = 'blog_post.html'
    return render(request, template_name, data)

def about(request):
    print 'GETTING ARTICLE'
    template_name = 'blog_about.html'
    return render(request, template_name, {})

def submit(request):
    template_name = 'blog_submit.html'
    return render(request, template_name, {})



def contributor_page(request, author_id):
    this_author =  get_object_or_404(Author,id=author_id)
    articles =  Post.objects.filter(authors__name=this_author.name)
    all_posts_sorted = list(reversed(sorted(articles, key=lambda i: i.created)))

    blog_page = paginate_posts(request, all_posts_sorted)

    data = {
        'posts': blog_page,
        'posts_data': list(blog_page),
        'name': this_author.name
    }
    template_name = 'blog.html'
    return render(request, template_name, data)


def tag_page(request, slug):
    this_tag =  get_object_or_404(Tag,slug__iexact=slug)
    data = {}
    data["author"] = this_tag.name
    data["articles"] =  Post.objects.filter(tags__name=this_tag.name)
    template_name = 'blog_tags.html'
    return render(request, template_name, data)


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog_post.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)
    })


def sections(request):
    section = request.path
    section = section.replace("/","").replace("blog","")

    data = {
        "name":section,
        "issues": []
    }
    if section == "writing":
        posts_in_cat = Post.objects.filter(posted__name__in= ["Writing","fiction","Lyric essay","Review essay","Interview"]).distinct()
    else:
        posts_in_cat = Post.objects.filter(posted__name = section)
    all_posts_sorted = list(reversed(sorted(posts_in_cat, key=lambda i: i.created)))

    paginator = Paginator(all_posts_sorted, 12) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_page = paginator.page(paginator.num_pages)
    image_list = []

    data = {
        'posts': blog_page,
        'posts_data': list(blog_page),
        'name': section
    }
    template_name = 'blog.html'
    return render(request, template_name, data)

def individual_theme(request, theme_id):
    posts_in_cat = Post.objects.filter(theme__name = theme_id)
    all_posts_sorted = list(reversed(sorted(posts_in_cat, key=lambda i: i.created)))

    blog_page = paginate_posts(request, all_posts_sorted)
    data = {
        'posts': blog_page,
        'posts_data': list(blog_page),
        'name': theme_id
    }
    template_name = 'blog.html'
    return render(request, template_name, data)


def paginate_posts(request, posts):
    paginator = Paginator(posts, 12) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_page = paginator.page(paginator.num_pages)
    image_list = []

    return blog_page

    