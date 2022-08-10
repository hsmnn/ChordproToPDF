from .models import Song
from .serializers import SongSerializer

from rest_framework import generics

class SongList(generics.ListAPIView):
    """
    View all songs.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
