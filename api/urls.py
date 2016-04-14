from django.conf.urls import patterns, include, url
import views

from rest_framework import routers

router = routers.DefaultRouter()

# may not want to expose some of these permissions without some permissions
resources = {

    # blog resources
    r'author': views.AuthorViewSet,
    r'blog_tag': views.TagViewSet,
    r'category': views.CategoryViewSet,
    r'images': views.ImagesViewSet,
    r'theme': views.ThemeViewSet,
    r'post': views.PostViewSet,

    # contact resources
    # r'contact':views.ContactViewSet
    # r'interaction': views.InteractionViewSet

    # magazine resources
    r'issue': views.IssueViewSet,
    r'section': views.SectionViewSet,
    r'contributor': views.ContributorViewSet,
    r'tag': views.TagViewSet,
    r'content': views.ContentViewSet,
    r'article': views.ArticleViewSet,
    r'image': views.ImageViewSet,
    # r'donation': views.DonationViewSet,
    # r'subscriber': views.SubscriberViewSet,
    # r'purchase': views.PurchaseViewSet,
    r'shop_item': views.ShopItemViewSet,

}

for key, value in resources.iteritems():
    router.register(key, value)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'auth/', include('rest_framework.urls', namespace='rest_framework')),
)
