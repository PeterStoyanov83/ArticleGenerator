from django.db import models


class ArticleTopic(models.Model):
    class Meta:
        app_label = 'ArticleGenerator'
    title = models.CharField(max_length=255)


class GeneratedArticle(models.Model):
    topic = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

