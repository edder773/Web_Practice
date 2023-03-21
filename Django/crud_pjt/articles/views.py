from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from .forms import ArticleModelForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, request.FILES)
        if form.is_valid():
            # # 밑에는 ArticleForm일떄
            # # cleaned_data : form의 데이터를 파이썬 딕셔너리로 반환
            # data = form.cleaned_data
            # # 제목 : (사용자입력) 형태
            # data['title'] = '제목:' + data['title']
            # article = Article(**data)
            # article.save()
            article = form.save()
        return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleModelForm
        context = {
            'form' : form,
        }
        return render(request, 'articles/create.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            form.save()
        return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleModelForm(instance=article)
        context = {'article': article, 'form': form,}
        return render(request, 'articles/update.html', context)
