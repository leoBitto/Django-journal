from django.db import models
from django_quill.fields import QuillField

class Entry(models.Model):

    date_created = models.DateTimeField(
        auto_now_add=True, 
        editable=False,
        )

    paragraphs = QuillField(default=None)

    MOOD_CHOICES = [(i, str(i)) for i in range(-3, 4, 1)]
    mood = models.IntegerField(choices=MOOD_CHOICES, default=0)

    def __str__(self):
        return f"{self.date_entry} - Mood: {self.mood}"