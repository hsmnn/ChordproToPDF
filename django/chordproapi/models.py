from django.db import models
from datetime import date

# Create your models here.

class Song(models.Model):
    """Stores songs"""
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    base_key = models.CharField(max_length=2)
    tempo = models.IntegerField()
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    created_on = models.DateField(default=date.today)
    last_updated = models.DateTimeField(default=date.today)
    #updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="last_modifier")
    content = models.TextField()

    class Meta:
        # Set the table name.
        db_table = 'song'

        # Set the default ordering
        ordering = ['id']

    def __str__(self):
        return self.title
