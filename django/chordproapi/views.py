from .models import Song
from .serializers import SongSerializer

from rest_framework import generics

class SongList(generics.ListAPIView):
    """
    View all songs.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single Song and allowsupdates and deletion of a Song.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_url_kwarg = 'song_id'
