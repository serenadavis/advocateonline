from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from .models import Article, Issue # '.' signifies the current directory

# Create your views here.
def index(request):
	issue = Issue.objects.first()

# for each article with this issue id
	articles_in_issue = Article.objects.filter(issue=issue)
	data = {
		'fiction': [],
		'features': [],
		'poetry': [],
		'art': []
	}
	# for article in articles_in_issue:
	# 	data[article.section].append(article)

	#template_name = 'index_v1.html',
	template_name = 'current_issues.html'
	return render_to_response(template_name, data, context_instance=RequestContext(request))

def article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	data = {
		'article': article
	}
	template_name = 'article.html'
	return render_to_response(template_name, data, context_instance=RequestContext(request))

def issues(request):
	all_issues = Issue.objects.all()

	data = {
		'issues': all_issues
	}
	template_name = 'issues.html'
	return render_to_response(template_name, data, context_instance=RequestContext(request))

def masthead(request):
	template_name = 'about_us.html'
	return render_to_response(template_name, context_instance=RequestContext(request))