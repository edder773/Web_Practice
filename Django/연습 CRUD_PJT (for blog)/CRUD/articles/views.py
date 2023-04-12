from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    content = {'articles':articles}
    return render(request,"articles/index.html", content)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid(): #유효성 검사
           article = form.save(commit=False)
           article.user = request.user
           article.save()
           return redirect('articles:read', pk=article.pk)
    else:
        form = ArticleForm()
    content = {'form':form}
    return render(request, 'articles/create.html',content)
    
def read(request, pk):
    article = Article.objects.get(pk=pk) # pk값을 받아지정
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == article.user:
                article.delete()
                return redirect('articles:index')
        return redirect('articles:index')
    else :
        commentform = CommentForm()
        comment = article.comment_set.all()
        content = {'article': article, 'commentform' : commentform, 'comment': comment,}
        return render(request, 'articles/read.html', content)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:read', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
        content = {'form':form, 'article': article, }
        return render(request, 'articles/update.html', content)
    else :
        return redirect('articles:index')

def comment_create(request,pk):
    article = Article.objects.get(pk=pk)
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:read', article.pk)

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:read', article_pk)