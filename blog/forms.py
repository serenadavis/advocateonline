from django.forms import ModelForm

from ajax_select import make_ajax_field

from .models import Post, Tag

from haystack.forms import SearchForm

from django import forms

from .models import Miscellany

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

class ImageUploadForm(forms.Form):
  image = forms.ImageField()

class MiscForm(forms.ModelForm):
  #body_text = forms.CharField(label='Post', max_length=255)
  #link = forms.CharField(label='http://', max_length=255)
  #nickname = forms.CharField(label='Nickname', max_length=10)
  class Meta:
    model = Miscellany
    fields = ['body_text', 'link', 'nickname','image']
#post = Miscellany.objects.all()[0]
#form = MiscForm(instance=post)
#form.as_p()
    #fields = ['body_text', 'link', 'nickname']
