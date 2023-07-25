from django.db import models
from django.contrib.auth.models import User


### Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    is_bookmark = models.BooleanField(default=False)
