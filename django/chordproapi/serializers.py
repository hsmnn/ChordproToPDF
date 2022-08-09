from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'author', 'base_key', 'tempo', 'created_on', 'last_updated', 'content')