from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context import RequestContext
from .models import Post
from collections import OrderedDict
from itertools import chain
import json
import stripe
from django.conf import settings
import random

from .models import *

def main(request):
    """Main listing."""
    posts = Post.objects.all()
    all_posts_sorted = list(reversed(sorted(posts, key=lambda i: i.created)))

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
        'posts_data': list(blog_page)
    }    
    template_name = 'blog.html'
    return render_to_response(template_name, data, context_instance=RequestContext(request))
    
def post(request, slug):
    print 'GETTING ARTICLE'
    post = get_object_or_404(Post, slug__iexact=slug)
    data = {
        'post': post
    }
    print post
    template_name = 'blog_post.html'
    return render_to_response(template_name, data, context_instance=RequestContext(request))

def about(request):
    print 'GETTING ARTICLE'
    template_name = 'blog_about.html'
    return render_to_response(template_name, {}, context_instance=RequestContext(request))


def contributor_page(request, author_id):
    this_author =  get_object_or_404(Author,id=author_id)
    # author.name = name.replace("_", " ")
    # author.id = author_id
    data = {}
    data["author"] = this_author.name
    data["articles"] =  Post.objects.filter(authors__name=this_author.name)
    template_name = 'blog_contributor.html'
    return render_to_response(template_name, data, context_instance=RequestContext(request))


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog_post.html', {
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
    return render_to_response(template_name, data, context_instance=RequestContext(request))

def individual_theme(request):
    section = request.path
    section = section.replace("/","").replace("blog","")

    data = {
        "name":section,
        "issues": []
    }

    posts_in_cat = Post.objects.filter(theme__name = theme)
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
    template_name = 'blog_section.html'
    return render_to_response(template_name, data, context_instance=RequestContext(request))