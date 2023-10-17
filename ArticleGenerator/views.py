from django.http import HttpResponse
from ArticleGenerator.models import ArticleTopic

def list_topics(request):
    topics = ArticleTopic.objects.all()
    return HttpResponse(', '.join([t.title for t in topics]))