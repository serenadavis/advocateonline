from django.forms import ModelForm

from ajax_select import make_ajax_field

from .models import Content, Tag


class ContentForm(ModelForm):
    class Meta:
        model = Content

    contributors = make_ajax_field(Content, 'contributors', 'contributor')
    tags = make_ajax_field(Content, 'tags', 'tag')


