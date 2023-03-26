from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    content = {'articles':articles}
    return render(request,"articles/index.html", content)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid(): #유효성 검사
           article = form.save()
           return redirect('articles:read', pk=article.pk)
    else:
        form = ArticleForm()
    content = {'form':form}
    return render(request, 'articles/create.html',content)
    
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
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:read', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    content = {'form':form, 'article': article, }
    return render(request, 'articles/update.html', content)

