from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

class Post(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 30)
    created_date = models.DateTimeField()
    view_cnt = models.IntegerField()
    contents = models.TextField()
    photo = models.ImageField(default='media/default_image.png')

    def calculating_date(self):
        self.created_date = timezone.now()
        self.save()
