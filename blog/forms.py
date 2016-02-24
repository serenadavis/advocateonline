from django.forms import ModelForm

from ajax_select import make_ajax_field

from .models import Post, Tag

from haystack.forms import SearchForm

class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class BlogSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

    def search(self):
        print 'hello'
        sqs = super(BlogSearchForm, self).search()

        print 'hello'

        if not self.is_valid():
            return self.no_query_found()

        sqs = sqs.order_by(title)

        return sqs
