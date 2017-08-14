from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,
                                          null=True)

    def display_date(self):
        return self.published_date if self.published_date else self.created_date

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title
