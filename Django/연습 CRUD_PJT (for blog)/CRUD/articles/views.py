from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    content = {'articles':articles}
    return render(request,"articles/index.html", content)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:read', pk=article.pk)
    else:
        return render(request, 'articles/create.html')
    
def read(request, pk):
    article = Article.objects.get(pk=pk) # pk값을 받아지정
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else :
        content = {'article': article}
        return render(request, 'articles/read.html', content)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:read', pk=article.pk)
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)

