from django.db import models

class Content(models.Model):
    TYPE_CHOICES = [
        ('anime', 'Anime'),
        ('manga', 'Manga'),
        ('manhwa', 'Manhwa'),
    ]

    title = models.CharField(max_length=200)
    image = models.URLField(blank=True)
    content_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title