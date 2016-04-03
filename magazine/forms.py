from django import forms

from ajax_select import make_ajax_field

from .models import Content, Tag

from haystack.forms import SearchForm

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content

    contributors = make_ajax_field(Content, 'contributors', 'contributor')
    tags = make_ajax_field(Content, 'tags', 'tag')


class ContentSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

    def search(self):
        print 'hello'
        sqs = super(ContentSearchForm, self).search()

        print 'hello'

        if not self.is_valid():
            return self.no_query_found()

        sqs = sqs.order_by(title)

        return sqs

class UploadShopItemForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=4095)
    price = forms.CharField(max_length=32)
    imagefile = forms.FileField()

