from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Book(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    author = models.CharField(max_length=255)
    publish = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        print(98765434567)
        return reverse('book:book_details', args=[
                        self.publish.year,
                        self.publish.month,
                        self.publish.day,
                        self.slug

                       ])
