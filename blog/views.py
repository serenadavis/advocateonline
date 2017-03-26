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
from django.shortcuts import redirect
from django import forms
from django.shortcuts  import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import MiscForm
from .forms import ImageUploadForm
from django.db.models import F
#from django.urls import reverse


class ImageUploadForm(forms.Form):
  image = forms.ImageField()


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
    post = get_object_or_404(Post, slug__iexact=slug)
    data = {
        'post': post
    }
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


def tag_page(request, slug):
    this_tag =  get_object_or_404(Tag,slug__iexact=slug)
    data = {}
    data["author"] = this_tag.name
    data["articles"] =  Post.objects.filter(tags__name=this_tag.name)
    template_name = 'blog_tags.html'
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

def miscellany(request):
    #Miscellany.objects.filter().update(votes=F('votes')+1)
    #Miscellany.objects.filter(pk=pk).update(votes=F('votes')+1)
    all_miscellany = Miscellany.objects.all()
    data = {
        'miscellany': all_miscellany
    
    }
    template_name = 'blog_miscellany.html'
    #return HttpResponse(template_name.render(data))
    return render_to_response(template_name, data, context_instance=RequestContext(request))

#def vote(request, Miscellany_id):
#  Miscellany = get_object_or_404(Miscellany, pk=Miscellany_id)
#  Miscellany.votes += 1
#  Miscellany.save()
#  return HttpResponseRedirect('blog_miscellany.html',
#    args=(Miscellany.id,))

def submit(request):
  if request.method == 'POST':
    form = MiscForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('blog_miscellany.html')
  else:
    form = MiscForm()
  return render(request, 'blog_submit.html', {'form': form })


#class PostLoveView(View):
#  def post(self, request):
#    data = {}
#    user = request.user
#    post_id = int(request.POST['post_id'])
#    post = get_objects_or_404(Miscellany, id=post_id)
#    loved = PostLove.objects.get_or_create(post=post)
#    user_loved = get_object_or_none(PostLove, user=user, post=post)
#    if user_loved:
#      loved.user.remove(user)
#      PostLove.objects.filter(post=post).update(total_loves=F('total_loves')-1)
#      data['success'] = 'unloved'
#    else: 
#      loved.user.add(user)
#      PostLove.objects.filter(user=user,
#          post=post).update(total_loves=F('total_loves')+1)
#    retrun JsonResponse(data)


def vote(request, pk):
  Miscellany.objects.filter(pk=pk).update(votes=F('votes')+1)
  return redirect('blog_miscellany.html')
  #data['success'] = 'loved'
  #return JsonResponse(data)

  #if request.method == 'POST':
  #  form = ImageUploadForm(request.POST, request.FILES)
  #  if form.is_valid():
  #    m = Miscellany.objects.create(
  #        image = request.POST['image']
  #        )
      #m = Miscellany.objects.get(pk=course_id)
      #m.image = form.cleaned_data['image']
      #m.save()
  #  miscpost = Miscellany.objects.create(
  #      body_text=request.POST['body_text'],
  #      nickname=request.POST['nickname'],
  #      link=request.POST['link']
  #      ) 
   # return redirect("blog_miscellany.html")
  #else:
  #  return render_to_response("blog_submit.html",
   #     context_instance=RequestContext(request))
  




  #if request.method == 'GET':
  #  form = MiscForm()
    # template_name = 'blog_submit.html'
  #  return render_to_response("blog_submit.html", context_instance=RequestContext(request))

####
 # if request.method == 'POST':
 #   form = MiscForm(request.POST)
 #   if form.is_valid():
 #     miscpost = Miscellany.objects.create(
 #         body_text=request.POST['body_text'],
 #         nickname=request.POST['nickname'],
 #         link=request.POST['link'],
#
#          )
#      #body_text=form.cleaned_data['body_text']
#      #link=form.cleaned_data['link']
#      #nickname=cleaned_data['nickname']
#      #post=Miscellany.objects.create(body_text=body_text, link=link,
#      #    nickname=nickname)
#      return redirect("blog_miscellany.html")
#  else:
#    form = MiscForm()
#  return render(request, 'blog_submit.html',{'form':form})

   # form = ImageUploadForm(request.POST, request.FILES)
   # if form.is_valid():
   #   m = Miscellany.objects.get(pk=course_id)
   #   m.model_image = form.cleaned_data['image']
   #   m.save()


    #miscpost = Miscellany.objects.create(
    #  body_text=request.POST['body_text'],
    # nickname=request.POST['nickname'],
    # link=request.POST['link'],
    #  image=request.POST['image'],


    # if form.is_valid():
      #  m = Miscellany.objects.get(pk=course_id)
       # m.model_image = form.cleaned_data['image']
      #  m.save()
    
    
# def upload_pic(request):
#  if request.method == 'POST':
#    form = ImageUploadForm(request.POST, request.FILES)
#    if form.is_valid():
#      m = Miscellany.objects.get(pk=course_id)
#      m.model_image  = form.cleaned_data['image']
#      m.save()
#      return HttpResponse('image upload success')
#  return HttpResponseForbidden('allowed only via POST')
