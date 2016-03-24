from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
# from .models import Article, Content, Issue , Subscriber# '.' signifies the current directory
from .models import Article, Content, Image, Issue, Contributor # '.' signifies the current directory
from blog.models import Post, Author
from collections import OrderedDict
from itertools import chain
import json
import stripe
from django.conf import settings
import random

from haystack.query import SearchQuerySet
from haystack.views import SearchView
from haystack.forms import SearchForm
from django.shortcuts import redirect
from itertools import chain
import logging


logger = logging.getLogger("magazine")

# Create your views here.
def index(request):
  issue = Issue.objects.last()

  # for each article with this issue id
  articles_in_issue = Article.objects.published().filter(issue=issue)
  data = {
    'blog': { },
    'sections': { },
    'issue': issue,
  }
  # Put articles into their respective sections
  for article in articles_in_issue:
    SectionName = str(article.section).lower()
    if SectionName not in data['sections']:
      data['sections'][SectionName] = [article]
    else:
        data['sections'][SectionName].append(article)
  data['sections']['art'] =  Image.objects.published().filter(issue=issue)

  # Randomly choice an article for every section
  for key in data['sections']:
    if data['sections'][key]:
      data['sections'][key]= random.choice(data['sections'][key])
  posts = Post.objects.all()
  recent_blog = list(reversed(sorted(posts, key=lambda i: i.created)))[:2 ]
  data['blog']['post1'] = recent_blog[0]
  data['blog']['post2'] = recent_blog[1]
  template_name = 'index.html'
  return render_to_response(template_name, data, context_instance=RequestContext(request))

def article(request, id, slug):
  article = get_object_or_404(Article, id=id)
  data = {
    'article': article
  }
  template_name = 'article.html'
  return render_to_response(template_name, data, context_instance=RequestContext(request))

def content_piece(request, id):
  image = get_object_or_404(Content, id=id)
  # print image.contributors
  data = {
    'art_content': image
  }
  template_name = 'content.html'
  # if not data['art_content']:
  #   print "here"
  return render_to_response(template_name, data, context_instance=RequestContext(request))

def contributor_page(request, author_id, name):
  author =  get_object_or_404( Contributor, id=author_id, name = name.replace("_", " "))
  # author.name = name.replace("_", " ")
  # author.id = author_id
  data = {}
  data["author"] = author.name
  data["articles"] =  chain( Article.objects.filter(contributors=author) , Image.objects.filter(contributors=author))
  template_name = 'contributor.html'
  return render_to_response(template_name, data, context_instance=RequestContext(request))


def issues(request):
  all_issues = Issue.objects.all()
  season = {'Winter': 0, 'Spring': 1, 'Commencement': 2, 'Fall': 3}

  #all_issues_sorted = reversed(sorted(all_issues, key=lambda i: i.year))
  all_issues_sorted = reversed(sorted(all_issues, key=lambda i: i.year * 10 + season[i.issue]))
  data = {
    'issues': all_issues_sorted
  }
  template_name = 'issues.html'
  return render_to_response(template_name, data, context_instance=RequestContext(request))

def masthead(request):
  template_name = 'about_us.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def singleissue(request, season, year):
  template_name = 'singleissue.html'
  issue = get_object_or_404(Issue, issue__iexact=season, year=year)

  # TODO: Once we figure out contenttypes, bring back this line!
  # issue_content = Content.objects.filter(issue=issue)

  content = OrderedDict()

  articles_in_issue = Article.objects.published().filter(issue=issue)

  for article in articles_in_issue:
    SectionName = str(article.section).lower()
    if SectionName not in content:
     content[SectionName] = [article]
    else:
       content[SectionName].append(article)
  content['art'] =  Image.objects.published().filter(issue=issue)

  # issue_content = Article.objects.filter(issue=issue)
  # section = ('Features','Fiction','Poetry')

  # content = OrderedDict()
  # for s in section:
  #   content[s] = issue_content.published().filter(section__name=s)
  # content['Art'] =  Image.objects.published().filter(issue=issue)
  data = {
    'issue' : issue,
    'content_list' : content
    }

  return render_to_response(template_name, data, context_instance=RequestContext(request))

class FilterSearchView(SearchView):
        template_name = 'search/search.html'
        queryset = SearchQuerySet().all()
        form_class = SearchForm
        type_filter = 'all'

        def __call__(self, request, type_filter = None):

                self.request = request

                self.form = self.build_form()
                self.query = self.get_query()
                self.results = self.get_results()

                if type_filter is not None:
                        self.results = self.results.filter(section=type_filter)
                        self.type_filter = type_filter
                else:
                        self.type_filter = 'all'

                return self.create_response()

        def extra_context(self):
                return {'type_filter' : self.type_filter}

        def create_response(self):
                (pageinator, page) = self.build_page()

                context = {
                        'query' : self.query,
                        'form' : self.form,
                        'page' : page,
                        'pageinator' : pageinator,
                        'suggestion' : None,
                }

                context['suggestion'] = self.form.get_suggestion()

                #for dict in Contributor.objects.all():
                #        if (dict['name'] == self.query):
                #                print dict

                try:
                        return redirect(Article.objects.get(title = self.query))
                except Article.DoesNotExist:
                        pass

                try:
                        return redirect(Contributor.objects.get(name = self.query))
                except Contributor.DoesNotExist:
                        pass
                try:
                        return redirect(Post.objects.get(title = self.query))
                except Post.DoesNotExist:
                        pass
                try:
                        return redirect(Author.objects.get(name = self.query))
                except Author.DoesNotExist:
                        pass

                context.update(self.extra_context())
                return render_to_response(self.template, context, context_instance=self.context_class(self.request))


def subscribe(request):
  template_name = 'subscribe.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def gala(request):
  template_name = 'gala.html'
  return render_to_response(template_name, context_instance=RequestContext(request))


def stripeSubmit(request):
  # Get the credit card details submitted by the form
  token = request.POST['stripeToken']
  stripe.api_key = settings.STRIPE_SECRET_KEY
  # Create the charge on Stripe's servers - this will charge the user's card
  try:
    charge = stripe.Charge.create(
      amount=123, # amount in cents, again
      currency="usd",
      card=token,
      description="payinguser@example.com",
    )


    subscriber = Subscriber.objects.create(
      name=request.POST['name'],
      email=request.POST['email'],
      streetAddress1=request.POST['streetAddress1'],
      streetAddress2=request.POST['streetAddress2'],
      city=request.POST['city'],
      state=request.POST['state'],
      country=request.POST['country'],
      zipCode=request.POST['zipCode'],
      renew=request.POST['renew'],
      subscriptionType=request.POST['subscriptionType'],
    )
    return subscribe(request)
  except stripe.CardError, e:
    # The card has been declined
    pass

def sections(request):
  section = request.path
  section = section.replace("/","")

  # For all issues
  all_issues = Issue.objects.all()
  season = {'Winter': 0, 'Spring': 1, 'Commencement': 2, 'Fall': 3}
  all_issues = reversed(sorted(all_issues, key=lambda i: i.year))
  #all_issues_sorted = reversed(sorted(all_issues, key=lambda i: i.year * 10 + season[i.issue]))
  data = {
    "name":section,
    "issues": []
  }

  for issue in all_issues:
    articles_in_issue = Article.objects.published().filter(issue=issue, section__name =section)
    if section == "art":
      if articles_in_issue:
        articles_in_issue = list(chain(articles_in_issue,Image.objects.published().filter(issue=issue, section__name =section) ))
      else:
        articles_in_issue = Image.objects.published().filter(issue=issue, section__name =section)

    datum = {
      'obj':issue,
      'articles': articles_in_issue
      }

    data["issues"].append(datum)

  # for issue in data["issues"]:
  #   for article in issue["articles"]:
  #     print article.contributors.all()

  template_name = 'section.html'
  return render_to_response(template_name, data, context_instance=RequestContext(request))

def submit(request):
  template_name = 'submit.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def contact(request):
  template_name = 'contact_us.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def alumni(request):
  template_name = 'alumni.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def advertise(request):
  template_name = 'advertise.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def shop(request):
  all_issues = Issue.objects.all()
  season = {'Winter': 0, 'Spring': 1, 'Commencement': 2, 'Fall': 3}
  #all_issues_sorted = reversed(sorted(all_issues, key=lambda i: i.year))
  all_issues_sorted = reversed(sorted(all_issues, key=lambda i: i.year * 10 + season[i.issue]))
  data = {
    'issues': all_issues_sorted,
    'page': 'shop',
  }
  template_name = 'shop.html'
  return render_to_response(template_name, data, context_instance=RequestContext(request))

def onefifty(request):
  template_name = '150th.html'
  return render_to_response(template_name, context_instance=RequestContext(request))

def comp(request):
  template_name = 'comp.html'
  return render_to_response(template_name, context_instance=RequestContext(request))
