from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class news(models.Model):
    news_title = models.TextField(max_length=100)
    news_desc = HTMLField()
    news_slug = AutoSlugField(populate_from='news_title', default=None , unique=True, null  =  True)

# Create your models here.
