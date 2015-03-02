from django.forms import ModelForm

from ajax_select import make_ajax_field

from .models import Content, Tag

from haystack.forms import SearchForm

class ContentForm(ModelForm):
    class Meta:
        model = Content

    contributors = make_ajax_field(Content, 'contributors', 'contributor')
    tags = make_ajax_field(Content, 'tags', 'tag')



class ContentSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

    def search(self):
        sqs = super(ContentSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        sqs = sqs.order_by(title)

        return sqs
