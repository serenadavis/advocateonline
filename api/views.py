from rest_framework import viewsets

from blog import serializers as blog_serializers
from blog.models import Author, Category, Images, Theme, Post
from blog.models import Tag as BlogTag

from contacts import serializers as contact_serializers
from contacts.models import Contact, Interaction

from magazine import serializers as magazine_serializers
from magazine.models import Issue, Section, Contributor, Tag, Content, Article, Image, Donation, Subscriber, Purchase, ShopItem


# blog
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = blog_serializers.AuthorSerializer


class BlogTagViewSet(viewsets.ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = blog_serializers.TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = blog_serializers.CategorySerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = blog_serializers.ImagesSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = blog_serializers.ThemeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = blog_serializers.PostSerializer


# contacts
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = contact_serializers.ContactSerializer


class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = contact_serializers.InteractionSerializer


# magazine
class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = magazine_serializers.IssueSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = magazine_serializers.SectionSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = magazine_serializers.ContributorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = magazine_serializers.TagSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = magazine_serializers.ContentSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = magazine_serializers.ArticleSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = magazine_serializers.ImageSerializer


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = magazine_serializers.DonationSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = magazine_serializers.SubscriberSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = magazine_serializers.PurchaseSerializer


class ShopItemViewSet(viewsets.ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = magazine_serializers.ShopItemSerializer
