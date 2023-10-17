from django.core.management.base import BaseCommand
from ArticleGenerator.models import ArticleTopic, GeneratedArticle
from ArticleGenerator.gpt_service import generate_article



class Command(BaseCommand):
    help = 'Generates an article using GPT and saves it to the database'

    def handle(self, *args, **kwargs):
        topic = ArticleTopic.objects.order_by('?').first()  # Get a random topic
        article_content = generate_article(topic.title)  # Generate the article
        GeneratedArticle.objects.create(topic=topic, content=article_content)  # Save the article
