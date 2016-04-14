from models import Issue, Section, Contributor, Tag, Content, Article, Image, Donation, Subscriber, Purchase, ShopItem

from rest_framework.serializers import HyperlinkedModelSerializer


class IssueSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Issue


class SectionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Section


class ContributorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Contributor


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag


class ContentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Content


class ArticleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article


class ImageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Image


class DonationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Donation


class SubscriberSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber


class PurchaseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Purchase


class ShopItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShopItem



