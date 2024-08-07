from django.shortcuts import render
from .models import News

def news(request):
    news = News.objects.all()
    # Объединяем контексты в один словарь
    context = {
        'active_page': 'news',
        'news': news,
    }
    return render(request, 'news/news.html', context)
