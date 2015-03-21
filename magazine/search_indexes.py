from haystack import indexes
from .models import Content
from .models import Section

class ContentIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title')
    section = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)

    def prepare_section(self, obj):
        return obj.section.name

    def get_model(self):
        return Content

    def index_queryset(self, using=None):
        return self.get_model().objects.all().select_related('section')
