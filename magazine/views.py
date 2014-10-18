from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
# . signifies the current directory
<<<<<<< HEAD
from .models import Article
=======
from .models import Article, Issue
>>>>>>> 29f3c83e61fd871b1b08536c4a5ad4c66f71f3b7

# Create your views here.
def index(request):
	issue = Issues.objects.first()

# for each article with this issue id
	articles_in_issue = Article.objects.filter(issue=issue)
	data = {
		'fiction': [],
		'features': [],
		'poetry': [],
		'art': []
	}
	for article in articles_in_issue:
		data[article.section].appen(article)

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
