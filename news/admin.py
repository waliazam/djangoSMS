from django.contrib import admin
from news.models import news

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_desc')
    
admin.site.register(news, NewsAdmin)
# Register your models here.
