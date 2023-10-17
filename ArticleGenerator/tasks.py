# tasks.py
from celery import shared_task
from ArticleGenerator.models import ArticleTopic


@shared_task
def generate_article():
    topic = ArticleTopic.objects.order_by('?').first()
    # Generate an article based on the topic
