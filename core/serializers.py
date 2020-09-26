from .models import List, Item
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'done']

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        item_set = ItemSerializer(many=True)
        model = List
        fields = ['name', 'owner', 'url', 'item_set']


