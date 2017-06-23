from django.db import models

from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', editable=False)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
