from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.
#get article list
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'health_resources/article_list.html', {'articles': articles})
#get article detail from the article list
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'health_resources/article_detail.html', {'article': article})