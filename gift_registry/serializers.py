from .models import Group, Gift, Gifter
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['event_name', 'event_date', 'join_code', 'pub_date', 'slug']

class GiftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gift
        fields = ['group', 'title', 'reciever', 'desc', 'url', 'only_one']

class GifterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gifter
        fields = ['gift', 'group', 'name']