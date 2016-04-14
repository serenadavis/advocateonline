from models import Contact, Interaction

from rest_framework.serializers import HyperlinkedModelSerializer


class ContactSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Contact


class InteractionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Interaction
