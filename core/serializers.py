from .models import List, Item
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'done']

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        item_set = ItemSerializer(many=True)
        model = List
        fields = ['id', 'name', 'owner', 'url', 'item_set']


