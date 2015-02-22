from haystack import indexes
from .models import Content

class ContentIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title')
    
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Content

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
