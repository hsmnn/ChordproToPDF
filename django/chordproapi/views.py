from .models import Song
from .serializers import SongSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class SongList(APIView):
    """
    View all songs.
    """

    def get(self, request, format=None):
        """
        Return a list of all songs.
        """
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)