from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'author', 'base_key', 'tempo', 'created_by', 'created_on', 'last_updated', 'updated_by', 'content')