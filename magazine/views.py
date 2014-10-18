from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
# . signifies the current directory
from .models import Article

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
