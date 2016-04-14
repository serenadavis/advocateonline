from models import Author, Tag, Category, Images, Theme, Post

from rest_framework.serializers import HyperlinkedModelSerializer


# serializers for blog

class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = (
            'name',
            'slug'
        )

class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category


class ImagesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Images


class ThemeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Theme


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
