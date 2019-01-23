from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField('Date Published')
    date_updated = models.DateTimeField(blank = True, null = True)
    content = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    date_created = models.DateTimeField('Date')
    content = models.TextField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
